#!/bin/sh
./scripts/pad-font.py ttfs/*.ttf
./scripts/make-hires.py ttfs/Topaz_a1200_v1.0.ttf
./scripts/convert-to-webfont.py ttfs/*.ttf
mv ttfs/*.woff* fonts/
