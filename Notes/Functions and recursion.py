# Name: Functions and Recursions
# Author: Ethan C
# Date: Dec 6

def factorial(num: int) -> int:
    """Returns the result of the number's
    facorial using recursion

    Params:
    num - number we're calculating 

    Returns: 
        result
    """
    if num == 0 or num == 1:
        return 1
    elif num > 1:
        return factorial(num - 1) * num
    



print(factorial(2))