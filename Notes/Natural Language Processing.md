---
tags:
  - notes
  - natural-language-processing
  - 2O23
  - programming-level-2
---
# Natural Language Processing
#### Output
We can use a function to display text and symbols to the screen
WE use the `print()` function to display output

```python
	print("Your text goes here")
	```


# Headers 
Comments are pieces of text that are not interpreted by python
This means that the text is ignored
We use the # symbol to make comments

# Input
We grab information from the user using the `input`().
When we run the function, it does two things:
1. It waits for the user to write something or nothing
2. The user presses **Enter/Return** to indicate that they're finished

```python
input() 

input(<promput>)      # It prints out the prompt then waits
```

# Variables
Variables allow us to store information for the time that our app is running.

```python
bozos_favourite_food = input("What is your favourite food? ")
```

favourite_food -> name of the variable
= -> assignment operator
input... -> value

#### Naming
What you can do:
1. Name them with letters, numbers, underscores
2. names should start with a lowercase letter
What you can't do
1. You can't name them with spaces or symbols
2. You can't name them with certain names that are reserved
	1. e.g. if , while , for , and, or ...

A good name is something like this:

```python
favourite_food
fave_food
date_of_birth
student_number
```

Bad names are like this:
```python
Favourite_food
a
num
aa
aaa
```

# Strings

## Format Strings
If we want to evaluate inside of a string, we use *f-strings*.

```python
fave_food = input("What is your favourite food? ")

print(f"Ooooo, {fave_food} sounds good.)
```

# Design

*The Design Process* is the steps that we take when we create a solution to a problem.

There are four steps in our design process

## 1. Design our Algorithm in English (Or any human languages)
An *algorithm* is a sequence of steps to solve a problems.
In this class, *before* we start ANY programming, we write our steps in English.

## 2. Translate our Algorithm from English to Python
We'll translate our algorithm into proper Python.

## 3. Test our Python Algorithm
Check if it works *syntactically*. In other words we check to see if it BREAKS. 
Check if it works *semantically*. In other words, does our algorithm actually solve the problem.

# Lists

A list in Python is a collection of items
We can store different values in a list
**Order matters** in a list
## Creating A List
To make a list, we use brackets [ ] to surround our list
We separate out the items using , 
 
```python
some_list = ["John", "Tim", "Sara"]
```


## Access Elements in a List
We can grab things from lists using the bracket notation
In our example above, if I wanted to access "Tim", I would do the following

```python
some_list[1]    # "Tim"
some_list[2]    # "Sara"
some_list[-1]    # "Sara"
some_list[-2]    # "Tim"
```

Inside the brackets, we say the *index* of the value we want
Python uses *0-index* counting, which means we start counting at 0

# Modules

Modules are bits of code that we can use in Python
These bits of code aren't automatically included, so we need to *import* them into our code

# Boolean

# Conditionals

# Import
The port keyword loads the module into our file
"import s" should be at the **top of the file** under the **header**
## The time module
Time allows us to play around with anything related to time
We can pause our code using *time*

```python
import time

# Pause code for 1 second
time.sleep(1.5)
```
