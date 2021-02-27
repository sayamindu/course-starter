# Course material starter pack

This is the "starter pack" that I use for my course material. The `slides` directory contains a template for slides, and the `syllabus` directory contains a template for a syllabus.

The templates are written in [Markdown](https://en.wikipedia.org/wiki/Markdown) and are processed with [Pandoc](https://pandoc.org/) to generate PDF and self-contained HTML files that you can put in your course website and/or share with students.

In order to use the templates, you will need 
 * Pandoc
 * Python 3 (with pip and virtualenv)
 * GNU Make

I have only used this in GNU/Linux systems, if you are using this on any other operating system, this may not work out of the box.

## Slides

A sample set of slides is provided in the `sampleslide` directory. Copy that directory, edit the `slides.md` file, and type `make` in the directory to generate your slides. The name of the copied directory should start with _day_ (e.g., `day-01-introductions`).

The file `slides/common.mk` has a few variables at the top which you may want to tweak.

## Syllabus

The `syllabus` directory contains a template syllabus in the file `index.md`.

The `Makefile` in the `syllabus` directory contains some variables such as course number that you may want to change.

Typing `make` in the syllabus directory will generate a PDF version of the syllabus along with a self-contained HTML version. The PDF generation process requires LaTeX. More information on installing LaTeX for use with Pandoc can be found in Pandoc's [installation documentation](https://pandoc.org/installing.html).

### Generating course schedules

Among other things, the template uses [Pantable](https://github.com/ickc/pantable) to include a course schedule from the CSV file in the generated syllabus. In order to generate the CSV file (you can see a sample in `schedule.csv`), you can use the `utilities/schedulestarter.py` to generate a "starter" schedule CSV file. You can use the `-h` argument to understand how to use the tool.

```
$ python utils/schedulestarter.py -h
usage: schedulestarter.py [-h] -s STARTDATE -e ENDDATE -d DAYS -c COLS -o OUTPUT

Generates an empty class schedule CSV file

optional arguments:
  -h, --help            show this help message and exit
  -s STARTDATE, --startdate STARTDATE
                        First day of classes (YYYY-MM-DD)
  -e ENDDATE, --enddate ENDDATE
                        Last day of classes (YYYY-MM-DD)
  -d DAYS, --days DAYS  Comma-separated days of the week in numbers (e.g., 0,2 is Monday, Wednesday)
  -c COLS, --cols COLS  Comma-separated names of additional columns for the CSV file (e.g., Topic,"Read before class",Exercise)
  -o OUTPUT, --output OUTPUT
                        Output CSV file name (will be overwritten)
$ 

```
So, if I were to generate a schedule called `schedule.csv` for a course between 10th January 2021 (first day of classes) and 2nd May 2021 (last day of classes), meeting on Monday and Wednesday, with a column for the day's topic, I would use the following command:

```
$ python utils/schedulestarter.py -s 2021-01-10 -e 2021-05-02 -d 0,2 -c Topic -o schedule.csv 
```

This generates a CSV file of the form:

```
Date,Topic
"Monday, January 11",
"Wednesday, January 13",
"Monday, January 18",
"Wednesday, January 20",
"Monday, January 25",
[...]
"Monday, April 26",
"Wednesday, April 28",
```

A spreadsheet software can then be used to edit the CSV file (make sure that you save it as a CSV file). The file can then be included in the `syllabus.md` as per the Pantable [instructions](https://github.com/ickc/pantable#example).


### Sub-pages

I usually generate my syllabus as one single HTML page. However, in some courses, more pages may be needed (e.g., for assignment submission instructions). The file `page1.md` is an example of such a page, with the sample `index.md` including a link to it.

