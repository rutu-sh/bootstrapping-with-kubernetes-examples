export DOCKER_REGISTRY=rutush10 # Replace with your Docker Hub username

all:
	echo "make all has been disabled by default to avoid building all sub-apps at once. If that's what you want, uncomment the lines in the Makefile following this make message."
	# cd src && \
	# $(MAKE) all

.PHONY: build
build:
	# builds applications in the src directory
	# usage: make build APP=simple-restapi-server SUB_APP=python TAG=0.0.1
	cd src/$(APP)/$(SUB_APP) && \
	$(MAKE) build


run:
	# runs the applications built from the src directory
	# usage: make run APP=simple-restapi-server SUB_APP=python TAG=0.0.1
	cd src/$(APP)/$(SUB_APP) && \
	$(MAKE) run


stop:
	# stops the applications running from the src dir
	# usage: make stop APP=simple-restapi-server SUB_APP=python
	cd src/$(APP)/$(SUB_APP) && \
	$(MAKE) stop
