# Functions and Turtle
# Author: Ethan
# 28 November 2023

import turtle

burt = turtle.Turtle()
burt.color("lightgreen")
burt.shape("turtle")


def squared(num: float) -> float:
    """Returns the given number squared"""
    return num**2


def draw_square(side_length: float) -> None:
    for _ in range(4):
        burt.forward(side_length)
        burt.left(90)


def draw_tree(level: int, height: int) -> None:
    """A recursive function that draws a tree
    with initial given height

    Params:

    level - number representing levels of branches
    height - height of the main trunk in pixels
    """

    if level > 0:
        # 1. Draw the branch
        burt.forward(height)

        # 2. Turn to the left
        burt.left(39)

        # 3. Draw a smaller tree (current level - 1)
        draw_tree(level - 1, height / 1.5)

        # 4. Turn to the right
        burt.right(39 * 2)

        # 5. Draw a smaller tree (current level - 1)
        draw_tree(level - 1, height / 1.5)

        # 6. Move back to beginning
        burt.left(39)
        burt.back(height)
    else:
        # create a level 0 tree, which is a leaf
        original_colour = burt.color()
        burt.color("green")
        burt.stamp()
        burt.color(original_colour[0])


# Setting ARWilson to draw the tree
# burt.hideturtle()
burt.setheading(90)
burt.width(4)
burt.color("brown")
burt.shape("arrow")
burt.speed(3)

draw_tree(10, 150)

turtle.done()