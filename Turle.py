# Turle Example
# Author: Ubial
# 21 November 2023

import turtle

# Create a turtle that can be moved around the screen
FORWARD_MAGNITUDE = 20

# Make a turtle object
leonardo = turtle.Turtle()

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
        leonardo.forward(FORWARD_MAGNITUDE)
    elif command.strip(",.?!").lower() == "r":
        leonardo.right(90)

    elif command.strip(",.?!").lower() == "l":
        leonardo.left(90)
    elif command == "stop":
        done = True
