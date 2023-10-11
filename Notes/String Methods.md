Methods are functions that we can use on objects.

String methods allow us to modify strings. 

Say for example, we want to make all the characters of a string lowercase. 

```python
mr_ubial_yelling = "YOU SHOULD STFU"

print(mr_ubial_yelling.lower())
```

We can use string methods to help solve [[Syntax errors#Semantic Errors]]
## .lower ()
The *.lower()* method takes a strong and coverts all uppercase characters to lowercase.

## .upper ()
The .upper() method uppercases all the letters.

## .strip(chars)
The .strip() method removes characters from both the beginning and the end of the string 

```python
user_feeling = input("How are you feeling today?")

# "good!" "Good!" "good!!!!!"
if user_feeling.lower() == "good":
	print("That's great!")
```

## .split(str) ->  List
The .split() method splits a string into a list, separating the string based on the characters you give it.

```python
grocery_string = "eggs milk cheese"
grocery_list = grocery_str.split("")

```
