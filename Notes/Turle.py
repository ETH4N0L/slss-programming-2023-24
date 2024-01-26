# Turle 
# Author: Ethan C
# 21 November 2023

import turtle

FORWARD_MAGNITUDE = 20

# Turtle object
raphael = turtle.Turtle()

# Get some input from the user
print("""To give commands, type:
F - to go forward
L  - to turn left
R - to turn right.""")

done = False

while not False:
    command = input("Where should I go? ")
    # Move the turtle around based on that input
    if command.strip(",.?!").lower() == "f":
        raphael.forward(FORWARD_MAGNITUDE)
    elif command.strip(",.?!").lower() == "r":
        raphael.right(90)

    elif command.strip(",.?!").lower() == "l":
        raphael.left(90)
    elif command == "stop":
        done = True
