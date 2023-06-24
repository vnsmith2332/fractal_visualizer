# Fractal Visualizer User Manual

The fractal visualizer is a program that can produce different fractals. It is intended to be an aid in teaching math students
about complex numbers and fractals. This manual contains information on how to run the program, what the program outputs, and
how to troubleshoot the program.


## Running the Program

**Prerequisites:**
* The Fractal Visualizer is installed on your computer
* Python is installed on your computer
* You know the location of the Fractal Visualizer program on your computer

The Fractal Visualizer is run from the command line interface, or terminal. A terminal is a program on your computer that allows you to 
interact with your computer's operating system using text commands instead of a graphical user interface (GUI). 
From the terminal, you can interact with files and run programs, among other things.

To run the Fractal Visualizer, follow the instructions below:

1. Open the terminal on your computer. On Windows, this can be done by searching for "Command Prompt" or 
"Windows PowerShell" in the Start menu. On macOS or Linux, you can use the built-in Terminal application.


2. Navigate to the folder where the Fractal Visualizer program is located using the cd command. For example, if the Fractal Visualizer is saved in a 
folder called "my_programs" on your desktop, you can navigate to it by entering the following command in the 
terminal: `cd ~/Desktop/my_programs`. Note that this command may contain many folder names. That is fine. Add folders to 
the command until you are in the correct folder.


3. Once you are in the folder that contains the Fractal Visualizer, you can run the program by entering the following 
command in the terminal: `python main.py [FRACTAL_FILE [PALETTE_NAME]]`, where `FRACTAL_FILE` is the path to a fractal configuration
file and `PALETTE_NAME` is the name of a color palette (for more information on fractal configuration files, see the section
of this document titled "Fractal Configuration Files"). The two palettes supported by this program are:
   * PaletteOne
   * PaletteTwo
     * Specifying a palette not supported by this program will result in an error (see the section of this document titled
     "Common Issues and How to Fix Them")
   
   Both `FRACTAL_FILE` and `PALETTE_NAME` are optional; if they are excluded, a default fractal utilizing a default palette
will be generated.


4. After running the above command, a small window will appear on your screen. After a few seconds,
the fractal will slowly be displayed in this window. In the terminal, a bar will appear that shows how much progress the program
has made in displaying the fractal (see example below).
    ```
    [ 42%==============                   ]
    ```
    After the fractal is generated, several more messages will appear, informing you that the fractal has been completed,
    how long it took, and that it has been saved (see example below). The completed fractal will be available in the pop-up window.
    ```
   [100%=================================]
   Done in 22.793 seconds!
   Wrote picture phoenix.png
   Close the image window to exit the program
    ```
5. To end the program, simply close the pop-up window containing the fractal image. This will return you to the command line
prompt where you may repeat step three with the same or different fractal.

If you are still having trouble running the program, please see the section of this manual titled "Common Errors and How to Fix Them" 
for additional guidance.

## Inputs
### Fractal Configuration files
A fractal configuration file is a file that contains the information needed to generate a specific fractal. For example,
`mandelbrot.frac` or `julia.txt` are two possible files that might contain the information to generate the mandelbrot and julia fractals,
respectively. This program comes with several configuration files that you may use; however, you can also create your own.

#### Creating Fractal Configuration Files
Below is an example of what the julia fractal configuration file contains:
```
# The Julia fractal
type: julia
creal: -1.0125
cimag: 0.275
pixels: 1024
centerx: 0.0
centery: 0.0
axislength: 4.0
iterations: 78
```

In configuration files, each piece of information has a label, such as "type" or "iterations". A colon follows the label
and to the right of the colon is the label's value. **This format must be maintained or the program will not be able to 
visualize the fractal.** Any line starting with a "#" is a comment; you can add comments if you wish to make notes about 
the fractal or the contents of the configuration file.

Some labels and values are required by all configuration files, while some are only required by fractals of specific types:
* Labels/values required by all fractals:
  * `type`: the fractal's type. The Fractal Visualizer supports mandelbrot, mandelbrot4, phoenix, and julia type fractals
  * `pixels`: the number of pixels in the image
  * `centerx`: the center of the image, horizontally
  * `centery`: the center of the image, vertically
  * `axisLength`: width of the image
  * `iterations`: the number of times a fractal algorithm will be run before giving a default value


* Labels/values required by phoenix type fractals:
  * `preal`
  * `pimag`
  

* Labelss/values required by julia type fractals:
  * `preal`
  * `pimag`
  * `creal`
  * `cimag`

When creating your own configuration files, be sure to include all required fields for the fractal type you are creating;
the program will give an error if a required field or value is missing.

#### The Default Fractal
Supplying a fractal configuration file to the program is optional; when one is not provided, the program will display the
following message and generate a default fractal that follows a default color scheme:
```
FractalFactory: Creating default fractal
PaletteFactory: Creating default color palette
```


### Color Palette
The color palette is the name of the palette that will be used to generate the image. This program supports two palettes:
* PaletteOne
* PaletteTwo

If any palette other than those supported by the program is specified, the program will produce an error.

#### Default Palette
Supplying the palette name to the program is optional; when it is not provided, the program generates the specified fractal
(if any) with the default color scheme and will display the following message:
```
PaletteFactory: Creating default color palette
```

## Outputs

### Fractal Images
The program will generate the specified fractal image in a small pop-up window.

### Fractal Image Files
In addition to displaying the fractals to your screen, the program automatically saves the fractals as `.png` files, so they
are not lost when you end the program. These files are saved to the project directory.

## Common Issues and How to Fix Them

Below is a list of common issues/errors you may encounter while interacting with the Fractal Visualizer, along with a 
description of how to fix them:

### Bad File Path: `No such file or directory`
This message will occur when an invalid file path is entered at the command line. The error may appear when you are trying to enter
the directory containing `main.py`, when trying to run the program `main.py`, or when specifying a fractal configuration
file. In all cases, this error message means that the file path you entered does not exist or is inaccessible. 
It is most often caused by a typo in the path. Check your file path and ensure it is correct. If this does not fix the issue,
ensure that the user has permission to access the file.

### Errors in Fractal Configuration Files: `RuntimeError`
A `RuntimeError` will occur when information in the fractal configuration file is incorrect, missing, of the wrong type
(ex: a word instead of a number), or incorrectly formatted. An error message describing the problem with the configuration
file will appear along with the error. To fix this, revisit the configuration file and ensure that everything is formatted and
spelled correctly; that all necessary information is present; and that all information is of the right type.

### Unsupported Features: `NotImplementedError`
The `NotImmplementedError` occurs when a nonexistent palette is specified. To fix this error, ensure that a valid palette has
been specified, or specify no palette to use the default.


