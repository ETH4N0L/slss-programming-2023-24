In Python, data can be grouped in categories called Types. 

| Name            | Example            |
| ---             | ---                |
| string          | "Hello"            |
| list            | '1, 2, 3, 4'       |
| integers or int | 1 -10 23           |
| float           | 3.1415 -3.1415 1.0 |

An example of using these types of data:
```python 
favourite_food = "tempura"
my_age = 17
```

# Type Conversion
In Python, there are some *special functions* that allow us to change the type of something.
```python
intro_string = "My age is "     # type string
my age = 17                     # type string

# Aside
"My name is" + "Slim Shady"     # "My name is SlimShady"

print(intro_string + my+age)    # THIS BREAKS
```

We can use the following *built* in functions to convert into different types:

We can fix the example above in this way:
```python 
intro_string = "My age is"
my_age = 17

print(intro_string + str(my+age))        # "My age is 17"
print(intro_string + " " + str(my_age)). #
print(f"{intro_string}{my_age}")
```
