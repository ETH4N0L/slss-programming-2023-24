# Star Wars Bot
# Ethan C
# Oct 16 2023
import time

# Introduction
print("I will decide if you should join the dark side.")
time.sleep(1.5)

# Ask user if they like red
colour = input("Do you like the colour red? ").lower().strip("!.,")
time.sleep(1.5)

# Ask user if they like capes
capes = input("Do you like capes? ").lower().strip("!.,")
time.sleep(1.5)

# If user answers yes to either one questions, they're on the dark side
# Otherwise, they are on the lightside
if colour == "yes" or capes == "yes":
    print("Dark side it is!")
else:
    print("Light side, I see.")