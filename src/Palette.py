from colour import Color
from math import ceil


class Palette:
    def get_color(self, n):
        raise NotImplementedError("Concrete subclass of Palette must implement getColor() method")


class PaletteOne(Palette):
    def __init__(self, fractal_info):
        base_colors = [Color("red"),
                       Color("white"),
                       Color("orange"),
                       Color("blue"),
                       Color("magenta"),
                       Color("green"),
                       Color("white"),
                       Color("yellow"),
                       Color("purple"),
                       Color("red"),
                       Color("yellow"),
                       Color("cyan")]

        # construct len(base_colors) - 1 mini palettes and concatenate them into one complete palette
        colors_per_mini_palette = (ceil(fractal_info["iterations"] / (len(base_colors) - 1))) + 1
        palette = []
        for i in range(len(base_colors) - 1):
            palette += list(Color.range_to(base_colors[i], base_colors[i + 1], colors_per_mini_palette))
            palette.pop()

        # correct palette length and get string representations
        while len(palette) > fractal_info["iterations"]:
            palette.pop()
        self.__palette = [color.get_hex_l() for color in palette]

    def get_color(self, n):
        """
        Given an index, n, return the color at palette[n]
        """
        return self.__palette[n]

    def __len__(self):
        return len(self.__palette)

    def get_palette(self):
        return self.__palette


class PaletteTwo(Palette):
    def __init__(self, fractal_info):
        base_colors = [Color("cyan"),
                       Color("yellow"),
                       Color("blue"),
                       Color("white"),
                       Color("purple"),
                       Color("green"),
                       Color("orange"),
                       Color("purple"),
                       Color("yellow"),
                       Color("brown"),
                       Color("lime"),
                       Color("red")]

        # construct len(base_colors) - 1 mini palettes and concatenate them into one complete palette
        colors_per_mini_palette = (ceil(fractal_info["iterations"] / (len(base_colors) - 1))) + 1
        palette = []
        for i in range(len(base_colors) - 1):
            palette += list(Color.range_to(base_colors[i], base_colors[i + 1], colors_per_mini_palette))
            palette.pop()

        # correct palette length and get string representations
        while len(palette) > fractal_info["iterations"]:
            palette.pop()
        self.__palette = [color.get_hex_l() for color in palette]

    def get_color(self, n):
        """
        Given an index, n, return the color at palette[n]
        """
        return self.__palette[n]

    def __len__(self):
        return len(self.__palette)

    def get_palette(self):
        return self.__palette
