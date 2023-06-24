import unittest
import os
from FractalParser import parse_fractal


class TestParser(unittest.TestCase):
    def setUp(self) -> None:

        self.julia_config = """\
# The full Julia set in all its glory
# You'll need to implement this formula yourself so your program can produce this image
type: julia
creal: -1.0125
cimag: 0.275
pixels: 1024
centerx: 0.0
centery: 0.0
axislength: 4.0
iterations: 78"""

        self.julia_dict = {"type": "julia",
                           "creal": -1.0125,
                           "cimag": 0.275,
                           "pixels": 1024,
                           "centerx": 0.0,
                           "centery": 0.0,
                           "axislength": 4.0,
                           "iterations": 78,
                           "min": {"x": -2,
                                   "y": -2},
                           "max": {"x": 2,
                                   "y": 2},
                           "pixelsize": .00390625,
                           "imagename": "_TEST_JULIA_CONFIG.png"}

        self.phoenix_config = """\
# Phoenix Fractal by Brock

type: phoenix
preal: -0.5
pimag: 0.0
# c value taken from http://usefuljs.net/fractals/docs/julia_mandelbrot.html, "Connected and Unconnected Sets"
creal: 0.5667
cimag: 0.0
centerx: 0
centery: 0
axislength: 3.25
pixels: 512
iterations: 101"""

        self.phoenix_dict = {"type": "phoenix",
                             "preal": -0.5,
                             "pimag": 0.0,
                             "creal": 0.5667,
                             "cimag": 0.0,
                             "centerx": 0.0,
                             "centery": 0.0,
                             "axislength": 3.25,
                             "pixels": 512,
                             "iterations": 101,
                             "min": {"x": -1.625,
                                     "y": -1.625},
                             "max": {"x": 1.625,
                                     "y": 1.625},
                             "pixelsize": .00634765625,
                             "imagename": "_TEST_PHOENIX_CONFIG.png"}

        self.mandelbrot_config = """\
# Basic mandelbrot set, fully zoomed out
type: mandelbrot
pixels: 640
centerx: 0.0
centery: 0.0
axislength: 4.0
iterations: 100"""

        self.mandelbrot_dict = {"type": "mandelbrot",
                                "pixels": 640,
                                "centerx": 0.0,
                                "centery": 0.0,
                                "axislength": 4.0,
                                "iterations": 100,
                                "min": {"x": -2,
                                        "y": -2},
                                "max": {"x": 2,
                                        "y": 2},
                                "pixelsize": .00625,
                                "imagename": "_TEST_MANDELBROT_CONFIG.png"}

        self.fileName_julia = "_TEST_JULIA_CONFIG.txt"
        self.fileName_phoenix = "_TEST_PHOENIX_CONFIG.txt"
        self.fileName_mandelbrot = "_TEST_MANDELBROT_CONFIG.txt"

        with open(self.fileName_julia, "w") as f:
            print(self.julia_config, end="", file=f)

        with open(self.fileName_phoenix, "w") as f:
            print(self.phoenix_config, end="", file=f)

        with open(self.fileName_mandelbrot, "w") as f:
            print(self.mandelbrot_config, end="", file=f)

        self.no_iterations_config = """\
# Phoenix Fractal by Brock

type: phoenix
preal: -0.5
pimag: 0.0
# c value taken from http://usefuljs.net/fractals/docs/julia_mandelbrot.html, "Connected and Unconnected Sets"
creal: 0.5667
cimag: 0.0
centerx: 0
centery: 0
axislength: 3.25
pixels: 512"""

        self.bad_type_float_config = """\
# Phoenix Fractal by Brock

type: phoenix
preal: -0.5
pimag: word
# c value taken from http://usefuljs.net/fractals/docs/julia_mandelbrot.html, "Connected and Unconnected Sets"
creal: 0.5667
cimag: 0.0
centerx: 0
centery: 0
axislength: 3.25
pixels: 512
iterations: 101"""

        self.bad_type_int_config = """\
# Phoenix Fractal by Brock

type: phoenix
preal: -0.5
pimag: 0.0
# c value taken from http://usefuljs.net/fractals/docs/julia_mandelbrot.html, "Connected and Unconnected Sets"
creal: 0.5667
cimag: 0.0
centerx: 0
centery: 0
axislength: 3.25
pixels: word
iterations: 101"""

        self.missing_colon_config = """\
# Phoenix Fractal by Brock

type: phoenix
preal: -0.5
pimag: 0.0
# c value taken from http://usefuljs.net/fractals/docs/julia_mandelbrot.html, "Connected and Unconnected Sets"
creal: 0.5667
cimag: 0.0
centerx: 0
centery: 0
axislength3.25
pixels: 512
iterations: 101"""

        self.missing_preal_config = """\
# Phoenix Fractal by Brock

type: phoenix
pimag: 0.0
# c value taken from http://usefuljs.net/fractals/docs/julia_mandelbrot.html, "Connected and Unconnected Sets"
creal: 0.5667
cimag: 0.0
centerx: 0
centery: 0
axislength: 3.25
pixels: 512
iterations: 101"""

        self.missing_creal_config = """\
# Phoenix Fractal by Brock

type: phoenix
preal: -0.5
pimag: 0.0
# c value taken from http://usefuljs.net/fractals/docs/julia_mandelbrot.html, "Connected and Unconnected Sets"
cimag: 0.0
centerx: 0
centery: 0
axislength: 3.25
pixels: 512
iterations: 101"""

        self.missing_value_config = """\
# Phoenix Fractal by Brock

type: phoenix
preal: -0.5
pimag: 0.0
# c value taken from http://usefuljs.net/fractals/docs/julia_mandelbrot.html, "Connected and Unconnected Sets"
creal: 0.5667
cimag: 0.0
centerx: 0
centery: 0
axislength: 3.25
pixels:
iterations: 101"""

        self.fileName_missing_value = "_TEST_MISSING_VALUE.txt"
        self.fileName_missing_creal = "_TEST_MISSING_CREAL.txt"
        self.fileName_missing_preal = "_TEST_MISSING_PREAL.txt"
        self.fileName_missing_colon = "_TEST_MISSING_COLON.txt"
        self.fileName_bad_type_int = "_TEST_BAD_INT.txt"
        self.fileName_bad_type_float = "_TEST_BAD_FLOAT.txt"
        self.fileName_no_iterations = "_TEST_NO_ITERATIONS.txt"

        with open(self.fileName_no_iterations, "w") as f:
            print(self.no_iterations_config, end="", file=f)
        with open(self.fileName_bad_type_float, "w") as f:
            print(self.bad_type_float_config, end="", file=f)
        with open(self.fileName_missing_preal, "w") as f:
            print(self.missing_preal_config, end="", file=f)
        with open(self.fileName_missing_creal, "w") as f:
            print(self.missing_creal_config, end="", file=f)
        with open(self.fileName_bad_type_int, "w") as f:
            print(self.bad_type_int_config, end="", file=f)
        with open(self.fileName_missing_value, "w") as f:
            print(self.missing_value_config, end="", file=f)
        with open(self.fileName_missing_colon, "w") as f:
            print(self.missing_colon_config, end="", file=f)

    def test_fractal_info(self):
        """
        Given a fractal configuration file, assert that parse_fractal() returns the expected dictionary
        """
        self.assertEqual(parse_fractal(self.fileName_julia), self.julia_dict)
        self.assertEqual(parse_fractal(self.fileName_mandelbrot), self.mandelbrot_dict)
        self.assertEqual(parse_fractal(self.fileName_phoenix), self.phoenix_dict)

    def test_exceptions(self):
        """
        Assert that FractalParser raises appropriate exceptions when errors are encountered in configuration files
        """
        with self.assertRaises(RuntimeError):
            parse_fractal(self.fileName_missing_value)
            parse_fractal(self.fileName_missing_creal)
            parse_fractal(self.fileName_missing_preal)
            parse_fractal(self.fileName_missing_colon)
            parse_fractal(self.fileName_bad_type_int)
            parse_fractal(self.fileName_bad_type_float)
            parse_fractal(self.fileName_no_iterations)

    def tearDown(self) -> None:
        os.remove(self.fileName_phoenix)
        os.remove(self.fileName_julia)
        os.remove(self.fileName_mandelbrot)

        os.remove(self.fileName_missing_value)
        os.remove(self.fileName_missing_creal)
        os.remove(self.fileName_missing_preal)
        os.remove(self.fileName_missing_colon)
        os.remove(self.fileName_bad_type_int)
        os.remove(self.fileName_bad_type_float)
        os.remove(self.fileName_no_iterations)


if __name__ == '__main__':
    unittest.main()
