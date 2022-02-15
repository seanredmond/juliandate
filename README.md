# juliandate

Simple conversions between [Julian
Dates](https://en.wikipedia.org/wiki/Julian_day) and Julian/Gregorian
calendar dates, supporting ancient dates (BCE)

## Installation

    pip install juliandate
    
## Usage

### Converting from Julian Date to Gregorian or Julian Calendar Date

A Julian Date such as `2440423.345486` indicates the number of days
(and fractional part) since noon January 1, 4713 BCE (Julian) or
November 24, 4714 BCE (Gregorian), a system proposed by [Joseph
Scaliger](https://en.wikipedia.org/wiki/Joseph_Justus_Scaliger)
in 1583. `2440423` is the number of full days, and the fractional
part, `0.345486` indicates that a little more than a third of a day
has passed (since noon).

To convert this to a Gregorian calendar date:

    >>> import juliandate as jd
    >>> jd.to_gregorian(2440423.345139)
	(1969, 7, 20, 20, 17, 0, 9609)
	
The return value is tuple consisting of the year, month, day, hour (in
24-hour format) minutes, seconds, and microseconds All are integers
and the last value is rounded to the nearest microsecond. This value,
`(1969, 7, 20, 20, 17, 0, 9609)`, means July 20, 1969 at 20:17 or 8:17
PM (when Apollo 11 touched down on the moon). There is some
imprecision in the seconds due to floating-point division.

For ancient dates, conversions to the [Julian
calendar](https://en.wikipedia.org/wiki/Julian_calendar) (and prior to
8 CE the [Proleptic Julian
Calendar](https://en.wikipedia.org/wiki/Proleptic_Julian_calendar))
are supported.

    >>> jd.to_julian(1705426)
	(-43, 3, 15, 12, 0, 0, 0)
	
The negative year indicates BCE. 1 BCE is 0, so -43 means 44 BCE, and
this value is March 15, 44 BCE (the Ides of March)

Note that since there is no fractional part of a day in `1705426`,
this comes out to noon, the start of the Julian Day. If we add half a
day or more, we will be into the next calendar day (March 16):

    >>> jd.to_julian(1705426.5)
	(-43, 3, 16, 0, 0, 0.0)
	
Conversions to the [Proleptic Gregorian
Calendar](https://en.wikipedia.org/wiki/Proleptic_Gregorian_calendar)
work as well. The Julian calendar date March 15, 44 BCE corresponds to
a Gregorian Calendar date of March 13:

    >>> jd.to_gregorian(1705426)
	(-43, 3, 13, 12, 0, 0)
	
	
### Converting from Gregorian or Julian Calendar Date to Julian Date

The reverse functions are:

    >>> jd.from_gregorian(1969, 7, 20, 20, 17, 0, 0)
    2440423.345138889
	
	>>> jd.from_julian(-43, 3, 15, 0, 0, 0, 0)
	1705425.5
	
Hours, minutes, seconds, and microseconds are optional so that latter could be:

	>>> jd.from_julian(-43, 3, 15)
	1705425.5

## The "Astronomical" Day

Julian dates begin at noon, the start of the [astronomical
day](https://en.wikipedia.org/wiki/Astronomical_day). This can lead to
some confusion since a calendar day, such as March 15 44 BCE, runs
from 1705425.5 (inclusive) to 1705426.5 (exclusive).

	# Midnight
    >>> jd.to_julian(1705425.5) 
	(-43, 3, 15, 0, 0, 0, 0)

	# 6 AM
    >>> jd.to_julian(1705425.75)
    (-43, 3, 15, 6, 0, 0, 0)
	
	# Noon
	>>> jd.to_julian(1705426)
	(-43, 3, 15, 12, 0, 0, 0)
	
	# 9 PM
	>>> jd.to_julian(1705426.25)
    (-43, 3, 15, 18, 0, 0, 0)
	
	# Midnight, next calendar day
    >>> jd.to_julian(1705426.5)
    (-43, 3, 16, 0, 0, 0, 0)
	
If all you care about is the calendar day, add 0.5 to the Julian Date
and take the integral part. This will return noon of the calendar
day. For example:

	# 6 AM
	>>> jd.to_julian(int(1705425.75 + 0.5))
	(-43, 3, 15, 12, 0, 0)	
	
	# Noon
	>>> jd.to_julian(int(1705426 + 0.5))
	(-43, 3, 15, 12, 0, 0)
	
	# 9 PM
	>>> jd.to_julian(int(1705426.25 + 0.5))
	(-43, 3, 15, 12, 0, 0)
	
## No `datetime` Objects

`juliandate` does not use Python `datetime` objects because these do
not support dates before 1 CE. Any date that _can_ be represented as a
Python `datetime` can easily be converted:

    >>> import juliandate as jd
	>>> from datetime import datetime
	>>> datetime(*jd.to_gregorian(2440423.345139))
	datetime.datetime(1969, 7, 20, 20, 17, 0, 9609)
	
	
## Imprecision

As noted above, floating-point math causes some imprecision in the
seconds and microseconds. This is unavoidable since 24ths and 60ths
don't divide equally. This round-trip, for instance, ends up being off
by 7 microseconds. Take care if this is important.

    >>> jd.to_gregorian(jd.from_gregorian(1969, 7, 20, 20, 17))
    (1969, 7, 20, 20, 16, 59, 999993)
	
You can check `juliandate`'s calculations against the US Naval
Observeratory's [Julian Date
Converter](https://aa.usno.navy.mil/data/JulianDate).
	
## Command Line Script

`juliandate` comes with a command-line script `jd` for converting Juliand Days

    $ jd 1705426.25
    -43, 3, 13, 18, 0, 0, 0
	
Use `jd -h` for more usage details.

## Contributing

Bug reports and pull requests are welcome on GitHub at
https://github.com/seanredmond/juliandate

