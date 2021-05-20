# Scikit-learn Prepackaged Model Server

## 1. Build the base image

```
$ make build
```

## 2. Your model directory structure for Primehub Deploy

The model server loads model with a named `model.joblib` file.

```
# Directory structure
.
└── model.joblib    
```

You can check the `gs://primehub-models/sklearn/iris` as a reference also.
