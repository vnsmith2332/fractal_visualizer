import unittest
from ImagePainter import ImagePainter
from PaletteFactory import palette_factory
from FractalFactory import fractal_factory


class TestImagePainter(unittest.TestCase):
    def setUp(self) -> None:
        fractal = fractal_factory()
        self._ImagePainter__fractal_info = fractal.get_fractal_info()
        palette = palette_factory(self._ImagePainter__fractal_info)

        self.ImagePainter = ImagePainter(fractal, palette, self._ImagePainter__fractal_info)

    def test_status_bar(self):
        """
        Assert that the progress bar produces correct output
        """
        self.assertEqual(ImagePainter.status_bar(self, 1), '[100% =================================]')
        self.assertEqual(ImagePainter.status_bar(self, 7), '[ 99% =================================]')
        self.assertEqual(ImagePainter.status_bar(self, 257), '[ 50% ================                 ]')
        self.assertEqual(ImagePainter.status_bar(self, 256), '[ 50% =================                ]')
        self.assertEqual(ImagePainter.status_bar(self, 100), '[ 80% ===========================      ]')
        self.assertEqual(ImagePainter.status_bar(self, 640), '[-25%                                  ]')
        self.assertEqual(ImagePainter.status_bar(self, 137), '[ 73% ========================         ]')
        self.assertEqual(ImagePainter.status_bar(self, 512), '[  0%                                  ]')


if __name__ == '__main__':
    unittest.main()
