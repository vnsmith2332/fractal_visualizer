from tkinter import Tk, Canvas, PhotoImage, mainloop
import sys
from time import time


class ImagePainter:
    def __init__(self, fractal, palette, fractal_info):
        self.__fractal = fractal
        self.__palette = palette
        self.__fractal_info = fractal_info

        self.__window = Tk()
        self.__tkPhotoImage = PhotoImage(width=self.__fractal_info["pixels"], height=self.__fractal_info["pixels"])
        tkCanvas = Canvas(self.__window, width=self.__fractal_info["pixels"], height=self.__fractal_info["pixels"], bg='#000000')
        tkCanvas.create_image((self.__fractal_info["pixels"]/2, self.__fractal_info["pixels"]/2), image=self.__tkPhotoImage, state="normal")
        tkCanvas.pack()

    def status_bar(self, row):
        """
        Display a status bar showing how much of the fractal has been rendered.
        """
        status_percent = '{:>4.0%}'.format((self.__fractal_info["pixels"] - row) / self.__fractal_info["pixels"])
        status_bar_width = 34
        progress_bar = '=' * int(status_bar_width * ((self.__fractal_info["pixels"] - row) / self.__fractal_info["pixels"]))
        progress_bar = '{:<33}'.format(progress_bar)
        return ''.join(list(['[', status_percent, ' ', progress_bar, ']']))

    def render_image(self):
        """
        Given a fractal's information, a tk window, and a PhotoImage object, render the fractal.
        """

        # for each pixel in each row, run either the phoenix or mandelbrot algorithm,
        # the complex coordinate being formed by x and y
        for row in range(self.__fractal_info["pixels"], 0, -1):
            cc = []
            for col in range(self.__fractal_info["pixels"]):
                x = self.__fractal_info["min"]["x"] + col * self.__fractal_info["pixelsize"]
                y = self.__fractal_info["min"]["y"] + row * self.__fractal_info["pixelsize"]

                cc.append(self.__palette.get_color(self.__fractal.count(complex(x, y))))

            # render the row
            self.__tkPhotoImage.put('{' + ' '.join(cc) + '}', to=(0, self.__fractal_info["pixels"] - row))
            self.__window.update()
            print(self.status_bar(row=row), end='\r', file=sys.stderr)

    def save_image(self):
        """
        Save a fractal image to a .png file
        """
        self.__tkPhotoImage.write(self.__fractal_info["imagename"])
        print("Wrote picture {}".format(self.__fractal_info["imagename"]))

    def main(self):
        """
        Obtain and pass fractal information to other functions
        """
        start_time = time()
        self.render_image()
        print(f"\nDone in {time() - start_time:.3f} seconds!")
        self.save_image()
        print("Close the image window to exit the program")
        mainloop()
