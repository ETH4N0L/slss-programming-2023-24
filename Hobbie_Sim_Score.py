# Hobbie Sim Score
# Author: Ethan
# Date: Nov 14

print("Please enter your hobbies, seperated by spaces. Ex. skiing drawing jogging")
Hobbies1 = input("Person 1: ")
Hobbies2 = input("Person 2: ")
Splitedhobbies1 = Hobbies1.lower().strip(",.!?").split()
Splitedhobbies2 = Hobbies2.lower().strip(",.!?").split()

similarity_score = 0

# Iterate through all movies in first list
for dahobbies in Splitedhobbies1:
    if dahobbies in Splitedhobbies2:
        similarity_score += 1

print(f"You have {similarity_score} hobbies in common!")