import sys
from ImagePainter import ImagePainter
from FractalFactory import fractal_factory
from PaletteFactory import palette_factory
from FractalParser import parse_fractal

# specified both config file and palette
if len(sys.argv) >= 3:
    fractal_info = parse_fractal(sys.argv[1])
    palette = palette_factory(fractal_info, sys.argv[2].lower().strip().replace(" ", ""))
    fractal = fractal_factory(fractal_info)
    image_painter = ImagePainter(fractal, palette, fractal_info)

# only specified config file
elif len(sys.argv) == 2:
    print("PaletteFactory: Creating default color palette")
    fractal_info = parse_fractal(sys.argv[1])
    fractal = fractal_factory(fractal_info)
    palette = palette_factory(fractal_info)
    image_painter = ImagePainter(fractal, palette, fractal_info)

# default fractal and palette
else:
    print("FractalFactory: Creating default fractal")
    print("PaletteFactory: Creating default color palette")
    fractal = fractal_factory()
    fractal_info = fractal.get_fractal_info()
    palette = palette_factory(fractal_info)
    image_painter = ImagePainter(fractal, palette, fractal_info)

image_painter.main()
