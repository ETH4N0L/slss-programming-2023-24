# Hobbie Sim Score
# Author: Ethan
# Date: Nov 15

print("Hi my offspring. ")
score = 0

eat = input("Did you eat? ").strip(".,!?").lower()
if eat == ("yes"):
    score +=1 

study = input("Did you study? ").strip(".,!?").lower()
if study == ("yes"):
    score +=1

laundry = input("Did you do your laundry? ").strip(".,!?").lower()
if laundry == ("yes"):
    score +=1

call = input("Did you call grandma? ").strip(".,!?").lower()
if call == ("yes"):
    score +=1

if score == 0:
    print("I'm coming over.")
elif score >= 1 and score < 2:
   print("Okay.")
else:
   print("Good!")