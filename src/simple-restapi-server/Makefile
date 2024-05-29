SUB_APPS := go python


.PHONY: all
all:
	for i in $(SUB_APPS); do \
		cd $$i && \
		$(MAKE) all \
		&& cd ..; \
	done
