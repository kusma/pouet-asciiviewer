#!/bin/python3

import os
import argparse
from fontTools.ttLib import TTFont

def main():
    parser = argparse.ArgumentParser(description='convert TTFs to webfonts')
    parser.add_argument('files', metavar='FILE', nargs='*')
    args = parser.parse_args()
    for file in args.files:
        font = TTFont(file)

        name = os.path.splitext(file)[0]
        font.flavor = "woff"
        font.save(name + ".woff")

        font.flavor = "woff2"
        font.save(name + ".woff2")

if __name__ == "__main__":
    main()
