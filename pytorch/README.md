# PyTorch Prepackaged Model Server

## 1. Build the base image

```
$ make build_rest
```

## 2. Your model directory structure for Primehub Deploy

`{model}.pt`, `{ModelClass}.py` can be replaced to any name. The `ModelClass.py` should contain the class named `PyTorchModel` which defines your model in the class.
```
# Directory structure
.
├── ModelClass.py
└── model.pt    
```

You can check the `gs://primehub-models/pytorch/CIFAR10` as a reference also.
