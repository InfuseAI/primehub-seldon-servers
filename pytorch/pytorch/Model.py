# Reference: https://github.com/kubeflow/kfserving/blob/master/python/pytorchserver/pytorchserver/model.py

import os, glob
import numpy as np
import torch
import importlib
import sys

class Model():
    def __init__(self, model_uri):
        self.ready = False
        self.model = None
        self.mlflow_autolog = False

        # check model exported from mlflow.pytorch.autolog()
        if os.path.isfile(os.path.join(model_uri, 'MLmodel')) and \
            os.path.isdir(os.path.join(model_uri, 'data')):
            print("Loading model from pytorch_lightning.Trainer.fit + mlflow.tensorflow.autolog()")
            model_uri = os.path.join(model_uri, 'data')
            self.mlflow_autolog = True

        print(model_uri)
        print(os.listdir(model_uri))

        self.device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
        self.model_class_name = 'PyTorchModel'
        
        py_files = []
        for filename in os.listdir(model_uri):
            if filename.endswith('.py'):
                py_files.append(filename)
        if len(py_files) == 1:
            self.model_class_file = os.path.join(model_uri, py_files[0])
        elif len(py_files) == 0:
            raise Exception('Missing PyTorch Model Class File.')
        else:
            raise Exception('More than one Python file is detected',
                            'Only one Python file is allowed within model_uri.')

        model_files = []
        for filename in os.listdir(model_uri):
            if filename.endswith('.pt') or filename.endswith('.pth'):
                model_files.append(filename)
        if len(model_files) == 1:
            self.model_file = os.path.join(model_uri, model_files[0])
        elif len(model_files) == 0:
            raise Exception('Missing PyTorch Model File.')
        else:
            raise Exception('More than one PyTorch Model file is detected',
                            'Only one PyTorch Model file is allowed within model_uri.')

        # Load the python class into memory
        sys.path.append(os.path.dirname(self.model_class_file))
        modulename = os.path.basename(self.model_class_file).split('.')[0].replace('-', '_')
        model_class = getattr(importlib.import_module(modulename), self.model_class_name)

        # Make sure the model weight is transform with the right device in this machine
        if self.mlflow_autolog:
            self.model = torch.load(self.model_file, map_location=self.device)
        else:
            self.model = model_class().to(self.device)
            self.model.load_state_dict(torch.load(self.model_file, map_location=self.device))
        self.model.eval()
        self.ready = True

    def predict(self, X, feature_names = None, meta = None):
        with torch.no_grad():
            try:
                inputs = torch.from_numpy(X).float().to(self.device)
            except Exception as e:
                raise TypeError(
                    "Failed to initialize Torch Tensor from inputs: %s, %s" % (e, inputs))
            try:
                if self.mlflow_autolog:
                    return self.model(inputs).detach().numpy()
                else:
                    return self.model(inputs).numpy()
            except Exception as e:
                raise Exception("Failed to predict %s" % e)

    def tags(self):
        return {}

    def class_names(self):
        return []

    def metrics(self):
        return []
