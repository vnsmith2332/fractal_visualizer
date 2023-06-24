class Fractal:
    def count(self, z):
        """
        Given a complex number return a count to be used in selecting a color from a palette
        """
        raise NotImplementedError("Concrete subclass of Fractal must implement count() method")

    def get_fractal_info(self):
        raise NotImplementedError("Concrete subclass of Fractal must implement get_fractal() method")


class Mandelbrot(Fractal):
    def __init__(self, fractal_info):
        self.__fractal_info = fractal_info

    def count(self, c):
        """
        Given a complex number return a count to be used in selecting a color from a palette
        """
        z = complex(0, 0)
        for i in range(self.__fractal_info["iterations"]):
            z = z * z + c
            if abs(z) > 2:
                if i >= self.__fractal_info["iterations"]:
                    i = self.__fractal_info["iterations"] - 1
                return i
        return self.__fractal_info["iterations"] - 1

    def get_fractal_info(self):
        return self.__fractal_info


class Mandelbrot4(Fractal):
    def __init__(self, fractal_info):
        self.__fractal_info = fractal_info

    def count(self, c):
        """
        Given a complex number return a count to be used in selecting a color from a palette
        """
        z = complex(0, 0)
        for i in range(self.__fractal_info["iterations"]):
            z = z ** 4 + c
            if abs(z) > 2:
                if i >= self.__fractal_info["iterations"]:
                    i = self.__fractal_info["iterations"] - 1
                return i
        return self.__fractal_info["iterations"] - 1

    def get_fractal_info(self):
        return self.__fractal_info


class Phoenix(Fractal):
    def __init__(self, fractal_info):
        self.__fractal_info = fractal_info

    def count(self, z):
        """
        Given a pixel in the form of a coordinate in the complex plain and the length of a color palette,
        return the index value of the pixel's color
        """
        JULIA_CONSTANT = complex(self.__fractal_info["creal"], self.__fractal_info["cimag"])
        PHOENIX_CONSTANT = complex(self.__fractal_info["preal"], self.__fractal_info["pimag"])

        z = complex(z.imag, z.real)
        z_previous = 0 + 0j

        for i in range(self.__fractal_info["iterations"]):
            z_save = z
            z = z * z + JULIA_CONSTANT + (PHOENIX_CONSTANT * z_previous)
            z_previous = z_save
            if abs(z) > 2:
                return i

        return self.__fractal_info["iterations"] - 1

    def get_fractal_info(self):
        return self.__fractal_info


class Julia(Fractal):
    def __init__(self, fractal_info):
        self.__fractal_info = fractal_info

    def count(self, z):
        """
        Given a complex number return a count to be used in selecting a color from a palette
        """
        c = complex(self.__fractal_info["creal"], self.__fractal_info["cimag"])
        for i in range(self.__fractal_info["iterations"]):
            z = z * z + c
            if abs(z) > 2:
                if i >= self.__fractal_info["iterations"]:
                    i = self.__fractal_info["iterations"] - 1
                return i
        return self.__fractal_info["iterations"] - 1

    def get_fractal_info(self):
        return self.__fractal_info
