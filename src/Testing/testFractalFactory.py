import unittest
from FractalFactory import fractal_factory


class TestFractalFactory(unittest.TestCase):
    def test_default_fractal(self):
        """
        Assert that fractal_factory returns a fractal object with the default properties
        """
        fractal_info = {"type": "julia",
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
        # print(fractal_factory().get_fractal_)
        self.assertEqual(fractal_factory().get_fractal_info(), fractal_info)

    def test_nonexistent_fractal(self):
        """
        Assert that supplying an unsupported fractal type in the config file results in a RuntimeError
        """
        fractal_info = {"type": "fake_fractal",
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
        with self.assertRaises(RuntimeError):
            fractal_factory(fractal_info)


if __name__ == '__main__':
    unittest.main()
