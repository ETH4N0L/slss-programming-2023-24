
# Initialize a list of continents
continents = ["Africa", "Antarctica", "Asia", "Europe", "North America", "South America", "Australia"]

# Initialize a variable to count visited continents
visited_count = 0

# Ask for the user's name
user_name = input("Hello! What's your name? ")

# Greet the user
print(f"Nice to meet you, {user_name}!")

# Use a for loop to ask about each continent
for continent in continents:
    while True:
        user_input = input(f"Have you been to {continent}? (Yes/No): ").strip().lower()
        if user_input == "yes":
            visited_count += 1
            break
        elif user_input == "no":
            break
        else:
            print("Invalid input! Please answer 'Yes' or 'No'.")

# Display the number of continents visited
print(f"{user_name}, you've been to {visited_count} out of 7 continents.")
        