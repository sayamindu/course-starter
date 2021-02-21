SUBDIRS := $(wildcard day*/.)

.PHONY: $(SUBDIRS)
.DEFAULT_GOAL := all

all: venv $(SUBDIRS)

clean: $(SUBDIRS)
	rm -rf venv

$(SUBDIRS):
	make -C $@ $(MAKECMDGOALS)

venv: venv/bin/activate

venv/bin/activate: requirements.txt
	test -d venv || virtualenv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/bin/activate
