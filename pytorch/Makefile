VERSION := v0.1.0
IMAGE_NAME_BASE=pytorch-prepackaged
IMAGE_BASE=infuseai/${IMAGE_NAME_BASE}

build_%:
	s2i build \
		-E environment_$* \
		./pytorch \
		seldonio/seldon-core-s2i-python3:0.18 \
		${IMAGE_BASE}_$*:${VERSION}

push_%:
	docker push ${IMAGE_BASE}_$*:${VERSION}

.PHONY: push_all
push_all: push_rest

.PHONY: build_all
build_all: build_rest
