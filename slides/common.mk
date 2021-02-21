# Based on on https://gist.github.com/kristopherjohnson/7466917
#

REVEALJS_THEME=black
COURSE="Course number, Term"

SOURCE_DOCS := $(wildcard *.md)

EXPORTED_DOCS=\
 $(SOURCE_DOCS:.md=.html)

PANDOC=source ../venv/bin/activate; /usr/bin/pandoc
PANDOC_OPTIONS=--standalone --resource-path=.:../commonassets:pandoc-templates
PANDOC_REVEAL_OPTIONS=--self-contained --filter ../filters/revealcode.py \
	-t revealjs --template ../pandoc-templates/default.revealjs --no-highlight \
	-V theme=$(REVEALJS_THEME)
PANDOC_VARIABLES=-V date=$(COURSE)

# Pattern-matching Rules
%.html : %.md
	$(PANDOC) $(PANDOC_OPTIONS) $(PANDOC_REVEAL_OPTIONS) $(PANDOC_VARIABLES) -o $@ $<

# Targets and dependencies
.PHONY: all clean

all : $(EXPORTED_DOCS)

clean:
	- rm -f $(EXPORTED_DOCS)
