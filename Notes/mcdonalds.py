# Mcdonalds
# Author: Ethan C
# Date: Nov 7 2023
import time

#Greet customer
print ("Hello there, welcome to McDonalds.")
time.sleep (1)
# Initialize variables for order and total cost
order = 0
total_cost = 0

# Ask the user if they want a burger
user_input = input("Do you want a burger for $5? (Yes/No): ").strip(",.?!").lower()
if user_input == "yes":
    total_cost += 5
    order += 1
if user_input == "no":
    print("Okay, that's fine.")
else: 
    print("Please input a valid answer.")

# Ask the user if they want fries
user_input = input("Do you want fries for $3? (Yes/No): ").strip(",.?!").lower()
if user_input == "yes":
    total_cost += 3
    order += 1
if user_input == "no":
    print("Okay, that's fine.")
else: 
    print("Please input a valid answer.")

# Calculate the total cost with tax (14%)
tax_rate = 0.14
total_with_tax = total_cost + (total_cost * tax_rate)

# Display the order and total cost
if order > 0:
    print("You ordered:",)
    print(f"Total cost before tax: ${total_cost:.2f}")
    print(f"Total cost with 14% tax: ${total_with_tax:.2f}")
else:
    print("You didn't order anything or you didn't input valid answers.")