A function is a block of code that can be reused over and over again. 

We can input data to the function.We refer to the data as parameters.

We describe the parameters in the docstring. A docstring (is short for documentation string) tells a human what the purposes of the funciton is. 

We use the term *arguments* to describe the ACTUAL data that we put into the function.

```python
def area_of_a_square()(sidelenght: float):
	""" Calculate and print the area of a square.
	Results in units squared.
	Params
sidelength - length of one side of the sqaure
"""

area = sidelength == 2

print(f"THe area of a quare with side length {sidelenght} is:
	 {area} square units.")
	print(f"the area of a square with side lenght {sidelenght} is
	{area} square units")
area_of_a_square(12.2)
```