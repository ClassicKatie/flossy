This project is designed to help create a pattern for counted cross stitch from a image file.  It imports the image, then examines the RGB values of each pixel then finds the DMC floss (thread color) with the nearest value.  The program then creates two HTML files with tables for the pattern: one contiguous pattern and one pattern divided up for 8.5x11 page size.  It also creates a legend at the end of the file.

The program will work with larger, photo-like pictures, but is really designed for smaller pixel art.  There are some commented-out lines that allow you to limit the size of the initial image.

There are two ways to run the program.  If you want to input an image and get a pattern back, run the program with the -p argument:

    python floss.py -p images/snowglobe.png

When done, the terminal will output the dimensions of the pattern in printable pages.  You can then find the contiguous pattern as renderedchart.html or the printable pattern as printchart.html

To find the DMC floss with the closest color to a single RGB value, run the program with -r -g -b arguments:

    python floss.py -r 200 -g 5 -b 50
