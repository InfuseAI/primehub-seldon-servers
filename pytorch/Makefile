VERSION := v0.2.0-dev
IMAGE_NAME_BASE=pytorch-prepackaged
IMAGE_BASE=infuseai/${IMAGE_NAME_BASE}

build:
	docker build . -t ${IMAGE_BASE}:${VERSION}

push:
	docker push ${IMAGE_BASE}:${VERSION}

