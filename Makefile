override APP_NAME = alcf
override APP_VERSION = 1.1.4
override FULL_TAG_LOCAL = $(APP_NAME):$(APP_VERSION)

.PHONY: docker-build
docker-build:
	docker image build -f Dockerfile --rm --tag $(FULL_TAG_LOCAL) .