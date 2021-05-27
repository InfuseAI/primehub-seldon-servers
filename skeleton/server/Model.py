class Model:
    def __init__(self, model_uri=None):
        # initialization
        # 1. configure model path from the model_uri if needed
        self.model_uri = model_uri
        self.model = None

        # 2. initialize the predictor
        # you might want to enable GPU if it is not enabled automatically

        # 3. invoke load method to preload the model
        self.ready = False
        self.load()

    def load(self):
        # load and create a model
        # if model_uri was given, load data and create model instance from it
        if self.ready:
            return

        # build model
        # 1. set to self.model
        # 2. make set.ready = True
        self.ready = True

    def predict(self, X, feature_names = None, meta = None):
        # execute self.model.predict(X)
        print(X, feature_names, meta)
        return "Hello Model"
