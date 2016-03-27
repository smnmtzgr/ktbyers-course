#!/usr/bin/env python

import pprint

# Easier to store these as constants
MINUTE_SECONDS = 60
HOUR_SECONDS = 60 * MINUTE_SECONDS
DAY_SECONDS = 24 * HOUR_SECONDS
WEEK_SECONDS = 7 * DAY_SECONDS
YEAR_SECONDS = 365 * DAY_SECONDS

uptime1 = 'twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes'
uptime2 = '3750RJ uptime is 1 hour, 29 minutes'
uptime3 = 'CATS3560 uptime is 8 weeks, 4 days, 18 hours, 16 minutes'
uptime4 = 'rtr1 uptime is 5 years, 18 weeks, 8 hours, 23 minutes'

uptime_dict = {}

for uptime in (uptime1, uptime2, uptime3, uptime4):
    uptime_split = uptime.split(',')

    uptime_seconds = 0

    for value in uptime_split:
        if ' years' in value:
            year = value.split()[-2]
            try:
                uptime_seconds += int(year) * YEAR_SECONDS
            except ValueError:
                print "Error, during string conversion to integer"

        if ' weeks' in value:
            week = value.split()[-2]
            try:
                uptime_seconds += int(week) * WEEK_SECONDS
            except ValueError:
                print "Error, during string conversion to integer"

        if ' days' in value:
            day = value.split()[-2]
            try:
                uptime_seconds += int(day) * DAY_SECONDS
            except ValueError:
                print "Error, during string conversion to integer"

        if ' hours' in value:
            hour = value.split()[-2]
            try:
                uptime_seconds += int(hour) * HOUR_SECONDS
            except ValueError:
                print "Error, during string conversion to integer"

        if ' minutes' in value:
            minute = value.split()[-2]
            try:
                uptime_seconds += int(minute) * MINUTE_SECONDS
            except ValueError:
                print "Error, during string conversion to integer"

    uptime_dict[uptime_split[0].split()[0]] = uptime_seconds

# Do the final printing to standard output
print
pprint.pprint(uptime_dict)
print
