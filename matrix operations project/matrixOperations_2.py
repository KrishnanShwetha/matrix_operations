#
# Images as 2-D lists  
#
# 

from hmcpng import *

def create_uniform_image(height, width, pixel):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels have the RGB values
        given by pixel
        inputs: height and width are non-negative integers
                pixel is a 1-D list of RBG values of the form [R,G,B],
                     where each element is an integer between 0 and 255.
    """
    pixels = []

    for r in range(height):
        row = [pixel] * width
        pixels += [row]

    return pixels

def blank_image(height, width):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels are green.
        inputs: height and width are non-negative integers
    """
    all_green = create_uniform_image(height, width, [0, 255, 0])
    return all_green

def brightness(pixel):
    """ takes a pixel (an [R, G, B] list) and returns a value
        between 0 and 255 that represents the brightness of that pixel.
    """
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    return (21*red + 72*green + 7*blue) // 100

## put your functions below
def grayscale(pixels):
    """Code for the function grayscale(pixels) that takes the 2-D list
    pixels containing pixels for an image, and that 
    creates and returns a new 2-D list of pixels for 
    an image that is a grayscale version of the original image.
    """
    height=len(pixels)
    width=len(pixels[0])
    grey_image=blank_image(height, width)
    for h in range(height):
        for w in range(width):
            grey_image[h][w]=pixels[h][w]
            grey_colour=brightness(pixels[h][w])
            grey_image[h][w]=[grey_colour,grey_colour,grey_colour]
    return grey_image

def fold_diag(pixels):
    """Code for the function fold_diag(pixels) that takes the 2-D list pixels 
    containing pixels for an image, and that creates and returns 
    a new 2-D list of pixels for an image in which the original image
    is “folded” along its diagonal.

    """
    height=len(pixels)
    width=len(pixels[0])
    folded_image=blank_image(height, width)
    for h in range(height):
        for w in range(width):
           folded_image[h][w]=pixels[h][w] 
           if h>w:
               folded_image[h][w]=[255,255,255]
    return folded_image

def mirror_horiz(pixels):
    """Code for the function mirror_horiz(pixels) that takes the 2-D list pixels 
    containing pixels for an image, and that creates and returns 
    a new 2-D list of pixels for an image in which the original image
    is “mirrored” horizontally.
    """
    height=len(pixels)
    width=len(pixels[0])
    mirrored_image=blank_image(height, width)
    for h in range(height):
        for w in range(width):
            mirrored_image[h][w]=pixels[h][w]
    for h in range(height):
        for w in range(width//2,width-1):
            mirrored_image[h][w]=pixels[h][(width-1)-w]  
    return mirrored_image

def  extract(pixels, rmin, rmax, cmin, cmax):
    """Code for the function extract(pixels, rmin, rmax, cmin, cmax) that takes 
    the 2-D list pixels containing pixels for an image, and that
    creates and returns a new 2-D list that represents the portion 
    of the original image that is specified by the other four parameters.
    """
    height=range(rmin,rmax)
    width=range(cmin,cmax)
    
    extracted_image=blank_image(len(height),len(width))
    
    for h in range(rmin,rmax):
        for w in range(cmin,cmax):
            extracted_image[h-rmin][w-cmin]=pixels[h][w]
    
    return extracted_image