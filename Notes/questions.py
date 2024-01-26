# 1.
def stars(num_stars: int):
    return "*" * num_stars

print(stars(5))

# 2
def biggest_of_three(num_one: float, num_two: float, num_three: float):
    """Returns the biggest of three given numbers.

    Params: 
    num_one - the first number
    num_two - the second number
    num_three - the third number

    Returns: 
    the biggest of the three numbers
    """
    if num_one > num_two and num_one > num_three:
        return num_one
    elif num_two > num_one and num_two > num_three:
        return num_two
    else:
        return num_three
    
    print(biggest_ofthree(1000, 100, 10))