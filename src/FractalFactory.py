from Fractal import Phoenix, Mandelbrot, Mandelbrot4, Julia

DEFAULT_FRACTAL = {"type": "julia",
                   "creal": .26,
                   "cimag": .0015,
                   "centerx": 0,
                   "centery": 0,
                   "axislength": 2.17,
                   "pixels": 512,
                   "iterations": 64,
                   "min": {"x": -1.085,
                           "y": -1.085},
                   "max": {"x": 1.085,
                           "y": 1.085},
                   "pixelsize": 0.00423828,
                   "imagename": "unconnected.png"}

def fractal_factory(fractal_info=DEFAULT_FRACTAL):
    """
    Given a fractal information dictionary, determine the fractal's type, call the appropriate constructor, and
    return the fractal object
    """
    if fractal_info["type"] == "mandelbrot":
        return Mandelbrot(fractal_info)
    elif fractal_info["type"] == "mandelbrot4":
        return Mandelbrot4(fractal_info)
    elif fractal_info["type"] == "phoenix":
        return Phoenix(fractal_info)
    elif fractal_info["type"] == "julia":
        return Julia(fractal_info)
    else:
        raise RuntimeError("The invalid fractal type '{}' was specified in the fractal configuration file".format(fractal_info["type"]))
