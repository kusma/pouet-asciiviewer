#!/bin/python3

from fontTools.ttLib import TTFont

font = TTFont('TopazPlus_a1200_v1.0.ttf')

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

font.flavor = "woff"
font.save("./topaz_a1200-hires.woff")

font.flavor = "woff2"
font.save("./topaz_a1200-hires.woff2")
