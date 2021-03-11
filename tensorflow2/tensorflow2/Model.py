import os, glob
import numpy as np
import tensorflow as tf
from io import BytesIO
from PIL import Image

class Model():
    def __init__(self, model_uri):
        print(model_uri)
        print(os.listdir(model_uri))

        self.loaded = False
        self.model_uri = model_uri

    def load(self):
        model_uri = self.model_uri
        self.use_keras_api = 1
        if tf.saved_model.contains_saved_model(model_uri):
            self.model = tf.saved_model.load(model_uri).signatures["serving_default"]
            if 'saved_model' not in str(type(self.model)):
                self.use_keras_api = 0
            else:
                del self.model
        if self.use_keras_api:
            if not glob.glob(os.path.join(model_uri, '*.h5')):
                self.model = tf.keras.models.load_model(model_uri)
            else:
                self.model = tf.keras.models.load_model(glob.glob(os.path.join(model_uri, '*.h5'))[0])
        self.loaded = True
        print(f"Use Keras API: {self.use_keras_api}")
        print(f"Model input layer: {self.model.inputs[0]}")

    def predict(self, X, feature_names = None, meta = None):
        if not self.loaded:
            self.load()
        if isinstance(X, bytes):
            img = Image.open(BytesIO(X))
            img = np.array(img).astype(np.float32)
            X = np.copy(img)
            X /= 255.0
            X = np.expand_dims(X, axis=0)

        if self.use_keras_api:
            return self.model.predict(X)
        else:
            output = self.model(tf.convert_to_tensor(X, self.model.inputs[0].dtype))
            return output[next(iter(output))].numpy()
