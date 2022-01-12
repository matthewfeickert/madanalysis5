default: test

all: test

BASE_IMAGE = python:3.9-slim-bullseye

test:
	docker pull $(BASE_IMAGE)
	docker build \
		--file docker/Dockerfile \
		--build-arg BUILDER_IMAGE=$(BASE_IMAGE) \
		--tag madanalysis5/madanalysis5:debug-local \
		.
