## Example prepackaged-server

Here is a skeleton to create a new prepackaged model server.

```bash
$ tree
.
|-- Dockerfile
|-- Makefile
|-- README.md
|-- example_model
`-- server
    |-- Model.py
    `-- requirements.txt
```

## build and push

There is a Makefile to build and publish the image

```
make build publish
```

Don't forget to modify the image tag in the Makefile

```makefile
VERSION := v0.1.0-dev
IMAGE_NAME_BASE=example-prepackaged
IMAGE_BASE=infuseai/${IMAGE_NAME_BASE}

build:
	docker build . -t ${IMAGE_BASE}:${VERSION}

push:
	docker push ${IMAGE_BASE}:${VERSION}
```

## Implement model server

```dockerfile
ENV MODEL_NAME Model
```

You should implement the new model server in the `server/Model.py` the name is defined in the Dockerfile `ENV`. It works in that way:

1. load python module `Model.py`
2. check if there is a class named `Model` in the loaded module.
3. create the instance `Model(**parameters)`


```python
# create a user_model and delegate client calls to it
user_model = Model(**parameters)

# load model if load method implemented
user_model.load()

# response the result of the predict method
user_model.predict(features, feature_names, **kwargs)
```

## load method

The `load` method is used to load a model file or a model directory and build the model instance.

Please consider to support the `model_uri` in your prepackaged server:

```python
def init(self, model_uri=None):
    self.model_uri = model_uri

def load(self):
    if self.model_uri:
        # load model from model_uri
        pass
    else:
        # load model from container
        pass
```

The `model_uri` is a mounted path in the `/mnt/models`, you should implement `load` method to load model from it.

### work with MLflow model

When you create a PrimeHub Deployment from a MLflow model, it will set `model_uri` to MLflow model registry path `models:/example/1` which will mount to `/mnt/models` with a `MLmodel` file. 

You could implement `load` method as if:

1. if the `MLmodel` file exists, treat it as MLflow model
2. if the `MLmodel` file doesn't exist, load the model in the originial way

## predict

You could send request to ask for a prediction result:

```curl
curl -k -X POST \
    -H "Content-Type: application/json" \
    http://example.primehub.io/deployment/your-deployment/api/v1.0/predictions \
    -d '{"data": {}}'
```

The payload should be a valid [SeldonMessage](https://docs.seldon.io/projects/seldon-core/en/v1.1.0/reference/apis/prediction.html#proto-buffer-and-grpc-definition)