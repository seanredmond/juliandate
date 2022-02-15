#!/usr/bin/env python3

import argparse
import juliandate as jd


def convert(j, args):
    d = int(j + 0.5) if args.round else j
    c = jd.to_julian(d) if args.julian else jd.to_gregorian(d)

    if args.tabs:
        return "\t".join([str(x) for x in c])

    return ", ".join([str(x) for x in c])
    

def main():
    parser = argparse.ArgumentParser(description="Convert Julian Days to calendar days")
    parser.add_argument("jds", metavar='J', type=float, nargs='*',
                        help="Julian days to convert")
    parser.add_argument("-f", "--file", type=argparse.FileType('r'),
                        help="Read from file or stdin ('-')")
    parser.add_argument("-j", "--julian", action="store_true",
                        help="Convert to Julian date instead of Gregorian")
    parser.add_argument("-r", "--round", action="store_true",
                        help="Round to simple day")
    parser.add_argument("-t", "--tabs", action="store_true",
                        help="Separate output with tabs instead of commas")

    args = parser.parse_args()

    if args.file is None:
        for j in args.jds:
            print(convert(j, args))

    else:
        for j in args.file:
            try:
                print(convert(float(j), args))
            except ValueError:
                pass


if __name__ == "__main__":
    main()
