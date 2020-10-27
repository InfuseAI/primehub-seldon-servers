# Tensorflow2 Prepackaged Model Server

## How to build the base image

```
$ make build_rest
```

## How to use base image to build image with model file

### SavedModel
- Create Dockerfile and change the value of ${MODEL} to your model name (my-model).
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
FROM infuseai/tensorflow2-prepackaged_rest:v0.1.0
COPY ${MODEL} /mnt/models
env model_url /mnt/models
```
```
# Build image
docker build -t tensorflow2-prepackaged-model .
```

### HDF5
- Create Dockerfile and change the value of ${MODEL} to your model name (my-model.h5).
```
# Directory structure
.
├── Dockerfile
└── my-model.h5
```
```
# Dockerfile
FROM infuseai/tensorflow2-prepackaged_rest:v0.1.0
COPY ${MODEL} /mnt/models
env model_url /mnt/models
```
```
# Build image
docker build -t tensorflow2-prepackaged-model .
```
