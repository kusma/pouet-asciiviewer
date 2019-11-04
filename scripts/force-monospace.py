#!/bin/python3

import os
import argparse
from fontTools.ttLib import TTFont

def main():
    parser = argparse.ArgumentParser(description='something something webfonts')
    parser.add_argument('files', metavar='FILE', nargs='*')
    args = parser.parse_args()
    for file in args.files:

        font = TTFont(file)



#for glyphName in font.getGlyphOrder():
#    glyphTable = font["glyf"]
#    glyph = glyphTable.glyphs.get(glyphName)
#    glyph.expand(glyphTable)
 
        glyphs = font.getGlyphSet()
        for key in glyphs.keys():
            value = glyphs[key]
            print("glyp width: " + key + ", " + str(value.width))
            # glyph.recalcBounds(glyphTable)

        hmtxTable = font['hmtx']
        correct_advance = (hmtxTable.metrics['A'][0], 0)
        for key, value in hmtxTable.metrics.items():
            print("advance: " + key + ", " + str(value))
            hmtxTable.metrics[key] = correct_advance

        name = os.path.splitext(file)[0]
        font.flavor = "woff"
        font.save(name + ".woff")

        font.flavor = "woff2"
        font.save(name + ".woff2")

if __name__ == "__main__":
    main()
