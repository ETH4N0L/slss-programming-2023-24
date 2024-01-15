from pathlib import Path
import csv

# File Exercises
# Author: Ethan Cheng
# Date: Nov 17 2023

"""Instructions:

Put this file in your programming folder.
Download the data-example.csv file and put it in this same folder.
For each problem, design a solution.
Each part builds on the previous step, so don't skip any.
You can refer to the work that we did last day for any hints.
Do not use any generative AI for the solutions."""

# Since our file has some symbols in it, this is the most
# effective way at opening up the file.

with open("./data_example.csv", encoding="utf-8") as f:
    lines = f.readlines()

# Note that I've set the encoding parameter to "utf-8"

# --- Problems


# Problem 1:
# Open the file contents of the second line in the file.

# Skip the first line (header) and get the second line
second_line = lines[1]

# Print the second line
print(second_line)

# Problem 2:
# Good! Now that you've done that, open the file, and print out every line of data.

for line in lines:
    print(line.strip())

# Problem 3:
# If you've made it this far, well done. Next task:
# Convert that line of data into a list.

# Create a list to store every line of data
data_list = []

# Store every line of data in the list
for line in lines:
    data_list.append(line.strip())  # Use strip() to remove leading and trailing whitespaces

# Print the list
print(data_list)

# Problem 4:
# Give yourself a pat on the back.
# See if you can count how many people like "Chicken Adobo" as their
# favourite food.

chicken_adobo_count = 0

# Iterate through each line and count occurrences of "Chicken Adobo"
for line in lines:
    if "Chicken Adobo" in line:
        chicken_adobo_count += 1

# Print the count
print(f"Num of people who like Chicken Adobo: {chicken_adobo_count}")

# Problem 5:
# You should have gotten four people for the last problem. If not,
# see if why your code doesn't work.
# Else, you can move on to this part, which is, find out how many
# people have the first letter of their first name start with "A".

# Initialize a counter for names starting with 'A'
a_starting_names_count = 0

# Iterate through each line and count occurrences of names starting with 'A'
for line in lines:
    # Assuming the first name is the first element in the CSV
    first_name = line.split(',')[0].strip()
    
    # Check if the first letter of the first name is 'A'
    if first_name.startswith('A'):
        a_starting_names_count += 1

# Print the count
print(f"Num of people that have A as the first letter of their fisrt names: {a_starting_names_count}")

# Problem 6:
# 19 people! Excellent. How many people come from Guangzhou?

guangzhou_count = 0

# Iterate through each line and count occurrences of "Chicken Adobo"
for line in lines:
    if "Guangzhou" in line:
        guangzhou_count += 1

# Print the count
print(f"Num of people who came from Guanzhou: {guangzhou_count}")

# Problem 7:
# Just one is from Guangzhou! Alright, last one. How many people have a credit card
# number that is even. There are a couple of ways to solve this.
# You can either do this with the string or with the int.


# Problem 8:
# Sorry, no answer for the above one. This one is a challenge question.
# Can you design a way to find the most popular food?
