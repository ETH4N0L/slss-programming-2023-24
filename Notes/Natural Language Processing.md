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

# Strings

## Format Strings
If we want to evaluate inside of a string, we use *f-strings*.

```python
fave_food = input("What is your favourite food? ")

print(f"Ooooo, {fave_food} sounds good.)
```