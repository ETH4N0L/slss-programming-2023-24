# Olympic Judging
# Author: Ethan C
# Date: Nov 7 2023

# Initialize a variable to store the total score
total_score = 0

# Get scores from 5 different judges
for i in range(5):
    score = float(input(f"Enter the score from Judge {i + 1} (0-10): "))
    if 0 <= score <= 10:
        total_score += score
    else:
        print("Invalid input! Please enter a score between 0 and 10.")

# Calculate the average score
average_score = total_score / 5

# Display the average score
print(f"The average score is: {average_score:.1f}")