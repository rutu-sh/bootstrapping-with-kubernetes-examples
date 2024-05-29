DEFAULT_CONT_NAME=simple-restapi-server-py
APP_IMAGE_NAME=simple-restapi-server-py
DOCKER_REPO_NAME=simple-restapi-server-py

build-docker-context:
	@echo "Building docker context" && \
	cp -r ${CURDIR}/src ${CURDIR}/build 


clear-docker-context:
	@echo "Clearing docker context" && \
	rm -rf ${CURDIR}/build/src

.PHONY: build
build: build-docker-context
	@echo "Building app" && \
	cd ${CURDIR}/build && \
	docker build --no-cache -t ${APP_IMAGE_NAME}:$(TAG) . 
	$(MAKE) clear-docker-context

run:
	@echo "Running app" && \
	docker run --rm --name ${DEFAULT_CONT_NAME} \
		-p 8000:8000 \
		${APP_IMAGE_NAME}:$(TAG)

stop:
	@echo "Stopping app" && \
	docker container stop ${DEFAULT_CONT_NAME} && \
	docker container rm ${DEFAULT_CONT_NAME} 

publish: build
	@echo "Publishing app" && \
	docker tag ${APP_IMAGE_NAME}:$(TAG) ${DOCKER_REGISTRY}/$(DOCKER_REPO_NAME):$(TAG) && \
	docker push ${DOCKER_REGISTRY}/${APP_IMAGE_NAME}:$(TAG) && \
	echo "Published ${DOCKER_REGISTRY}/${APP_IMAGE_NAME}:$(TAG) successfully"


.PHONY: all
all:
	$(MAKE) build-app && \
	$(MAKE) publish