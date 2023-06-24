import unittest
from Palette import PaletteOne, PaletteTwo
from PaletteFactory import palette_factory


class TestPalettes(unittest.TestCase):
    def setUp(self) -> None:
        """
        Create Palette objects for testing
        """
        fractal_info = {"iterations": 512}
        self.paletteOne_512 = PaletteOne(fractal_info)

        fractal_info = {"iterations": 64}
        self.paletteOne_64 = PaletteOne(fractal_info)

        fractal_info = {"iterations": 400}
        self.paletteOne_400 = PaletteOne(fractal_info)

        fractal_info = {"iterations": 786}
        self.paletteOne_786 = PaletteOne(fractal_info)

        fractal_info = {"iterations": 1024}
        self.paletteTwo_1024 = PaletteTwo(fractal_info)

        fractal_info = {"iterations": 225}
        self.paletteTwo_225 = PaletteTwo(fractal_info)

        fractal_info = {"iterations": 653}
        self.paletteTwo_653 = PaletteTwo(fractal_info)

        fractal_info = {"iterations": 125}
        self.paletteTwo_125 = PaletteTwo(fractal_info)

    def test_len_palette(self):
        """
        Assert that the length of palettes is the same as iterations
        """
        self.assertEqual(len(self.paletteOne_512), 512)
        self.assertEqual(len(self.paletteOne_64), 64)
        self.assertEqual(len(self.paletteOne_400), 400)
        self.assertEqual(len(self.paletteOne_786), 786)

        self.assertEqual(len(self.paletteTwo_1024), 1024)
        self.assertEqual(len(self.paletteTwo_225), 225)
        self.assertEqual(len(self.paletteTwo_653), 653)
        self.assertEqual(len(self.paletteTwo_125), 125)

    def test_default_palette(self):
        """
        Assert that palette_factory returns a palette of type PaletteTwo when no palette is specified
        """
        fractal_info = {"iterations": 512}
        self.assertEqual(type(self.paletteTwo_1024), type(palette_factory(fractal_info)))

    def test_color_types(self):
        """
        Assert that each palette contains only strings
        """
        for color in self.paletteOne_512.get_palette():
            self.assertEqual(type(color), type("string"))

        for color in self.paletteTwo_1024.get_palette():
            self.assertEqual(type(color), type("string"))

    def test_nonexistent_palette(self):
        """
        Assert that unsupported palettes raise NotImplementedError
        """
        fractal_info = {"iterations": 512}
        with self.assertRaises(NotImplementedError):
            palette_factory(fractal_info, "FAKE_PALETTE")


if __name__ == '__main__':
    unittest.main()
