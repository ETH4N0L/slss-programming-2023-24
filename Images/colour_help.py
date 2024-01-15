# Colour Helper
# Author: Ethan
# December 13 2023

# Do you need help with colours?
# This is for you!

from PIL import Image

def pixel_to_name(pixel: tuple) -> str:
    """Given a 3-tuple, return a string representing
    its colour

    Params:
        pixel = 3-tuple of values (red, green, blue)

    Returns:
        name of the colour
    """
    red, green, blue = pixel

    if red < 230 and blue < 230 and green > 150:
        return "green"
    else:
        return "colour unknown"

def is_light(pixel: tuple) -> bool:
# Check the average pixel colour
    average = sum(pixel) / len(pixel)

    # Check if the average is greater than or equal to 128
    return average >= 128

# Test cases
pixel1 = (200, 150, 100)
pixel2 = (50, 75, 100)

# Test the function with the provided test cases
print(is_light(pixel1))  # This should print True
print(is_light(pixel2))  # This should print False
black_pixel = (0, 0, 0)
dark_gray_pixel = (127, 127, 127)
light_gray_pixel = (128, 128, 128)
white_pixel = ( 255, 255, 255)

print(is_light(black_pixel)) # False
print(is_light(dark_gray_pixel)) # False
print(is_light(light_gray_pixel)) # True
print(is_light(white_pixel)) # True

# open up kid green
with Image.open("./Images/kid-green.jpg") as im:
    # create variables that store the width and height
    image_height = im.height
    image_width = im.width

    # load the background image
    bg_im = Image.open("./Images/beach.jpg")

    # outer loop is top->bottom
    # inner loop is left->right
    for y in range(image_height):
       for x in range(image_width):
           pixel = im.getpixel((x, y))

           # check pixel if it's green
           if pixel_to_name(pixel) == "green":
               # replace with bg_pixel
               bg_pixel = bg_im.getpixel((x, y))
               im.putpixel((x, y), bg_pixel)

bg_im.close()

# save the image 
im.save("./Images/output.jpg")


