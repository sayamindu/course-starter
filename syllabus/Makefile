# Based on on https://gist.github.com/kristopherjohnson/7466917
#

TEMPLATE_PATH=templates
COURSE="Course 000: Course Title"
TERM="Fall 20XX"
AUTHOR="Instructor Name"
INSTITUTION="Department, Institution"

SOURCE_DOCS := $(wildcard *.md)

EXPORTED_DOCS=\
 $(SOURCE_DOCS:.md=.html) \
 $(SOURCE_DOCS:.md=.pdf)

VENV_ACTIVATOR=source ./venv/bin/activate

PANDOC=$(VENV_ACTIVATOR); /usr/bin/pandoc
PANDOC_OPTIONS=--filter pantable --resource-path=.:$(TEMPLATE_PATH)
PANDOC_HTML_OPTIONS=--self-contained --standalone  --metadata author=$(AUTHOR) \
	--metadata date=`date +'%Y-%m-%d'` -t html5 --template template.html --toc --toc-depth=1 \
	--email-obfuscation=references
PANDOC_PDF_VARIABLES=-V documentclass=scrartcl -V fontfamily=libertine -V geometry:margin=1in \
	--metadata date='' -V colorlinks
PANDOC_VARIABLES=--metadata title=$(COURSE) \
	-V term=$(TERM) -V institution=$(INSTITUTION)

all: venv $(CSVFILES) $(EXPORTED_DOCS)

# Pattern-matching Rules
%.html : %.md
	$(PANDOC) $(PANDOC_OPTIONS) $(PANDOC_HTML_OPTIONS) $(PANDOC_VARIABLES) -o $@ $<
%.pdf : %.md
	$(PANDOC) $(PANDOC_OPTIONS) $(PANDOC_VARIABLES)  $(PANDOC_PDF_VARIABLES) -o $@ $<

CSVFILES := $(wildcard *.csv)

venv: venv/bin/activate

venv/bin/activate: requirements.txt
	test -d venv || virtualenv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/bin/activate

clean:
	- rm -f $(EXPORTED_DOCS)
	- rm -rf venv

.PHONY: all clean
