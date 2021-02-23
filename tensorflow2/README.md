# Tensorflow2 Prepackaged Model Server

## 1. Build the base image

```
$ make build
```

## 2. Use base image to build image with model file

### SavedModel
Create Dockerfile and change the value of `${MODEL}` to your model name (`my-model`).
```
# Directory structure
.
├── Dockerfile
└── my-model
    ├── saved_model.pb
    └── variables
        ├── variables.data-00000-of-00001
        └── variables.index
```
```
# Dockerfile
FROM infuseai/tensorflow2-prepackaged:v0.2.0-dev
COPY ${MODEL} /mnt/models
```
```
# Build image
docker build -t tensorflow2-prepackaged-model .
```

### HDF5
Create Dockerfile and change the value of `${MODEL}` to your model name (`my-model.h5`).
```
# Directory structure
.
├── Dockerfile
└── my-model.h5
```
```
# Dockerfile
FROM infuseai/tensorflow2-prepackaged:v0.2.0-dev
COPY ${MODEL} /mnt/models
```
```
# Build image
docker build -t tensorflow2-prepackaged-model .
```
