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

        for glyphName in font.getGlyphOrder():
            glyphTable = font["glyf"]
            glyph = glyphTable.glyphs.get(glyphName)
            glyph.expand(glyphTable)
            glyph.recalcBounds(glyphTable)
            coord = glyph.getCoordinates(glyphTable)[0]
            coord.scale((2.0, 1.0))
            glyph.recalcBounds(glyphTable)

        hmtxTable = font['hmtx']
        for key, value in hmtxTable.metrics.items():
            hmtxTable.metrics[key] = (value[0] * 2, value[1])

        name, ext = os.path.splitext(file)
        font.save(name + "-hires" + ext)

if __name__ == "__main__":
    main()
