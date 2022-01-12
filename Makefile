default: test

all: test

test:
	docker pull python:3.9-slim-bullseye
	docker build \
		--file docker/Dockerfile \
		--tag madanalysis5/madanalysis5:debug-local \
		.
