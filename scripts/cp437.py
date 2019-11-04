#!/bin/python3

import os
import argparse
import json

# this is very disappointing; seems Python's cp437 encoding is simply wrong
# about values 0 through 31 and 127, and interpret them as directly mapped
# to the corresponding unicode code-points. This table contains corrections
# on top of this
cp437_errors = {
    1: chr(0x263A), 2: chr(0x263B), 3: chr(0x2665), 4: chr(0x2666),
    5: chr(0x2663), 6: chr(0x2660), 7: chr(0x2022), 8: chr(0x25D8),
    9: chr(0x25CB), 10: chr(0x25D9), 11: chr(0x2642), 12: chr(0x2640),
    13: chr(0x266A), 14: chr(0x266B), 15: chr(0x263C), 16: chr(0x25BA),
    17: chr(0x25C4), 18: chr(0x2195), 19: chr(0x203C), 20: chr(0x00B6),
    21: chr(0x00A7), 22: chr(0x25AC), 23: chr(0x21A8), 24: chr(0x2191),
    25: chr(0x2193), 26: chr(0x2192), 27: chr(0x2190), 28: chr(0x221F),
    29: chr(0x2194), 30: chr(0x25B2), 31: chr(0x25BC), 127: chr(0x2302)
}

def get_cp437(x):
    if x in cp437_errors:
        return cp437_errors[x]
    return bytes([x]).decode('cp437')

def main():
    parser = argparse.ArgumentParser(description='"pad" font to avoid fallback-characters')
    parser.add_argument('files', metavar='FILE', nargs='*')
    args = parser.parse_args()

    cp437_codepoints = [ord(get_cp437(x)) for x in range(256)]
    with open('cp437.json', 'w') as outfile:
        json.dump(cp437_codepoints, outfile)

if __name__ == "__main__":
    main()
