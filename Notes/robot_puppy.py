# Robot Puppy
# Author: Ethan
# Date: Jan 12 2024

from PIL import Image

# Set the path of the image
image_path = './Images/Red Ball.jpeg'

# Define the function
def find_ball_center(image_path):
    image = Image.open(image_path)

# Convert the image to rgb
    rgb_image = image.convert('RGB')

# Provide the value of the colour red
    red_color = (255, 0, 0)

# List for all red pixels in image
    red_pixels = []
    width, height = image.size
    for x in range(width):
        for y in range(height):
            pixel = rgb_image.getpixel((x, y))
            red_pixels.append((x, y))

    # Calculate the center of the red pixels
    if red_pixels:
        center_x = sum(x for x, _ in red_pixels) // len(red_pixels)
        center_y = sum(y for _, y in red_pixels) // len(red_pixels)
        return center_x, center_y
    else:
        return None

center = find_ball_center(image_path)

print(f"Center of the red ball: ({center[0]}, {center[1]})")