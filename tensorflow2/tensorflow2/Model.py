import os, glob
import numpy as np
import tensorflow as tf

class Model():
    def __init__(self, model_uri):
        print(model_uri)
        print(os.listdir(model_uri))

        self.use_keras_api = 1
        if tf.saved_model.contains_saved_model(model_uri):
            self.model = tf.saved_model.load(model_uri).signatures["serving_default"]
            if type(self.model) == tf.python.eager.wrap_function.WrappedFunction:
                self.use_keras_api = 0
        if self.use_keras_api:
            if not glob.glob(os.path.join(model_uri, '*.h5')):
                self.model = tf.keras.models.load_model(model_uri)
            else:
                self.model = tf.keras.models.load_model(glob.glob(os.path.join(model_uri, '*.h5'))[0])
        print(f"Use Keras API: {self.use_keras_api}")
        print(f"Model input dtype: {self.model.inputs[0].dtype}")

    def predict(self, X, feature_names = None, meta = None):
        if self.use_keras_api:
            output = self.model.predict(X)
            return output
        else:
            output = self.model(tf.convert_to_tensor(X, self.model.inputs[0].dtype))
            return output['x'].numpy()

    def tags(self):
        return {}

    def class_names(self):
        return []

    def metrics(self):
        return []
