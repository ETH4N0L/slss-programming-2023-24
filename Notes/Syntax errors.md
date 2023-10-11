
These types of errors are ones where you run your code and something breaks.

Syntax errors are relatively easy to fix. 

If we forget a closing " or typed in the wrong name, we'll get a syntax error
Example:
```python
name = Ethan
print("Hi)
print(names)
```
SyntaxError: unterminated string literal (detected at line 1)
NameError: name 'names' is not defined. Did you mean: 'name'?

# Semantic Errors

Semantic errors are much more challenging to squash. 

Semantic errors are where you code doesn't "mean" what you actually mean.

```python
user_response = input("Do you like to eat food?")

if user_response == "yes":
	print("You passed the human test")
if user_response == "no":
	print("You failed the human test)")
```

The problem with the above code is subtle. What (MR. Ubial) mean is that if the user answers with anything affirmative, the code should go into the "yes" block.

One way to solve this problem is to use String Methods. We can use .lower() to catch all permutations of capital letters in the code semantic errors are when your code doesn't mean what you actually want it to mean.

```python
user_response = input("Do you like to eat food?")

if user_response.lower() == "yes":
	print("You passed the human test")
if user_response == "no":
	print("You failed the human test)")
```
