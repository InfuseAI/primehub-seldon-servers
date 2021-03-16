VERSION := v0.1.1-dev
IMAGE_NAME_BASE=tensorflow2-prepackaged
IMAGE_BASE=ej04xjp6/${IMAGE_NAME_BASE}

build:
	docker build . -t ${IMAGE_BASE}:${VERSION}

push:
	docker push ${IMAGE_BASE}:${VERSION}
