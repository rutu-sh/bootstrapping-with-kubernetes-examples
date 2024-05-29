SUBDIRS = simple-restapi-server

.PHONY: all
all:
	for i in $(SUBDIRS); do \
		cd $$i && $(MAKE) all && cd ..; \
	done

