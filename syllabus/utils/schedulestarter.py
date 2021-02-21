#!/usr/bin/env python
import argparse
import csv
import datetime

import dateutil.relativedelta as relativedelta
import dateutil.rrule as rrule

def parse_args():
    parser = argparse.ArgumentParser(description='Generates an empty class schedule CSV file')

    parser.add_argument('-s', '--startdate',
        type=datetime.datetime.fromisoformat,
        help="First day of classes (YYYY-MM-DD)",
        required=True)
    parser.add_argument('-e', '--enddate',
        type=datetime.datetime.fromisoformat,
        help="Last day of classes (YYYY-MM-DD)",
        required=True)
    parser.add_argument('-d', '--days',
        type=lambda days: [int(day) for day in days.split(',')],
        help='Comma-separated days of the week in numbers (e.g., 0,2 is Monday, Wednesday)',
        required=True)
    parser.add_argument('-c','--cols',
        type=lambda cols: [col.strip() for col in cols.split(',')],
        help='Comma-separated names of additional columns for the CSV file (e.g., Topic,"Read before class",Exercise)',
        required=True)
    parser.add_argument('-o', '--output',
        type=argparse.FileType('w'),
        help="Output CSV file name (will be overwritten)",
        required=True)

    args = parser.parse_args()

    return (args.startdate, args.enddate, args.days, args.cols, args.output)


if __name__ == '__main__':
    start, end, days, cols, csvfile = parse_args()

    rr = rrule.rrule(rrule.WEEKLY, byweekday=days, dtstart=start)
    days = rr.between(start, end, inc=True)

    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Date'] + cols)
    for day in days:
        csvwriter.writerow([day.strftime("%A, %B %d")] + ['']*len(cols))
    csvfile.close()
