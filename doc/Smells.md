# CS 1440 Assignment 5.0: Refactoring - Code Smells Report


## Code Smells Report

0. Bad Comments in `src/main.py` [lines 82-112]
   *    The ASCII art containing the phrase "CODE IS ART" is unnecessary and clutters the file.
   * ```python
        ###########################
        ####### CODE IS ART #######
        ###########################
        ```
   * Remove the commented ASCII art


1. Spaghetti Code in `src/main.py` [lines 52-122]
   *    The code to validate the user's input is unclear, messy, and difficult to understand
   *    ```python
        ### quit when the first one of the arguments isn't on the command line  	  	  
        arg_is_phoneix = 0  	  	  
        while sys.argv[1] in PHOENX:  	  	  
            arg_is_phoneix += True  	  	  
            break  	  	  
        sys.exit(True)  	  	  
        else:  	  	  
            arg_is_phoneix = False  	  	  
        sysargv1_not_mndlbrt_frctl = MBROTS.count(sys.argv[1])
        ```
   *    Rewrite input validation in `src/main.py`. This code can be rewritten to do what is needed in much fewer lines.


2. Dead Code in `src/phoenix_fractal.py` [lines 28-30]
   *    Imports unused libraries
   *    ```python
        import turtle  	  	  
        import os  	  	  
        import os.path 
        ```
   *    Remove these import statements


3. Complex Decision Tree in `src/main.py` [lines 159-167]
   *    Decision tree is unnecessarily complex and difficult to understand
   *    ```python
        if PHOENX.count(sys.argv[1])>0: phoenix.phoenix_main(sys.argv[1])  	  	  
        elif sys.argv[1] in MBROTS and len(sys.argv) > 1 and 2 <= len(sys.argv[0]):  	  	  
            fractal = sys.argv[1]  	  	  
            mbrot_fractal.mbrot_main(fratcal)  	  	  
        elif len(sys.argv) != 0 and fratcal in PHOENX and len(sys.argv) != 1:  	  	  
            phoenix.phoenix_main(fractal)  	  	  
        else: print("The fractal given on the command line",  	  	  
                    fractal,  	  	  
                    "was not found in the command line") 
         ```
   * Remove some boolean expressions to simplify the decision tree.

4. Too many arguments for a function in `src/pheonix_fractal.py` [line 129]
   *    The function signature contains far too many arguments, most of which are never used in the function body.
   *    ```python
        def makePictureOfFractal(f, i, e, w, g, p, W, a, b, s):  	  	  
            """Paint a Fractal image into the TKinter PhotoImage canvas.  	  	  
            Assumes the image is 640x640 pixels."""  
        ```
   *    Remove the unused arguments and give more descriptive names to the used arguments


5. Global Variable in `src/pheonix_fractal.py` [line 59]
   *    A global variable is present
   *    ```python
        s = 512 
        ```
   *    Remove the global variable and define it locally as needed


6. Poorly-Named Identifier in `src/mbrot_fractal.py` [line 103]
   *    The global constant `TWO` is unclearly named. It is not at all clear what this constant's purpose is from its name.
   *    ```python
        TWO = 2
        ```
   *    Investigate the constant, figure out its purpose, and provide a more descriptive name


7. Redundant Code in `scr/phoenix_fractal.py` [lines 331-341]
   *    The fractal image is saved as a `.png` file twice.
   *    ```python
        if Save_As_Picture:  	  	  
            # Write out the Fractal into a .gif image file  	  	  
            tkPhotoImage.write(i + ".png")  	  	  
            #tkPhotoImage.write(f"{i}.png")  	  	  
            print(f"\nDone in {time() - b4:.3f} seconds!", file=sys.stderr)  	  	  

        if Save_As_Picture:  	  	  
            # Output the Fractal into a .png image  	  	  
            tkPhotoImage.write(f"{i}.png")  	  	  
            print("Wrote picture " + i + ".png", file=sys.stderr)  	  	  
            #tkPhotoImage.write(f"{i}.png")
        ```
   *    Remove the second black that saves the file. Also consider creating a new function to perform this task


8. Function that is too Long in `src/mbrot_fractal.py` [lines 140-213]
   *    This function is far too long. It can return two different things, depending on the arguments passed in. Thus, it
   contains logic to do both things, lending to its length.
   *    ```python
        def PixelColorOrIndex(c, palette):  	  	  
            """  	  	  
            Return the color of the current pixel within the Mandelbrot set  	  	  
            - OR -  	  	  
            Return the INDEX of the color of the pixel within the Mandelbrot set  	  	  
            The INDEX corresponds to the iteration count of the for loop.  	  	  
            """  
        ```
   *    Investigate whether two return types are really needed; if so, split the two possible return types into two different functions.


9. Magic Numbers in `src/mbrot_fractal.py` [lines 236-247]
   *    The literals `512` and `256` are used frequently in this section without context as to their significance.
   *    ```python
        canvas.create_image((256, 256), image=img, state="normal")  	  	  

        # At this scale, how much length and height on the imaginary plane does one  	  	  
        # pixel take?  	  	  
        pixelsize = abs(maxx - minx) / 512  	  	  
        portion = 0  	  	  
        total_pixels = 512 * 512  # 262144  	  	  
        # loop  	  	  
        for row in range(512, 0, -1):  	  	  
            cc = []  	  	  
            for col in range(512):
        ```
   *    Investigate these numbers, figure out their significance, and use descriptive identifiers to reference them.
