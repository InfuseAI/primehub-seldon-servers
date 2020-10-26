import os
import tensorflow as tf

class Model():
    def __init__(self):
        model_url = os.environ["model_url"]
        self._model = tf.keras.models.load_model(model_url)
        print(self._model.summary())

    def predict(self, X, feature_names = None, meta = None):
        output = self._model.predict(X)
        return output

    def tags(self):
        return {}

    def class_names(self):
        return []

    def metrics(self):
        return []
