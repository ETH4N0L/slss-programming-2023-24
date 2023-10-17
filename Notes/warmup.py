# Crude Chatbot
# Author: Ethan C
# Date: 29 September
import time
import random
list_of_food_responses = [
        "I don't actually care, but cool I guess.",
        "Okay, very basic. Very boring. Bye.",
        f"You actually like this food? You're just begging to be made fun of.",
        "This is no one likes you. Even your taste in food is bad lol.",
        "Thanks for telling me but If I wasn't programmed to ask I wouldn't have."
]
# Choose one of those responses randomly
random_food_response = random.choice(list_of_food_responses)

print("I am Crudebot, here to lower my IQ talking to a dummy like you.")
time.sleep(1.5)
user_name = input("What's your name bud? ")
print(f"Okay {user_name}, what's your favourite food?")
fave_food = input("Don't worry, I WILL judge your tastes. ")

if fave_food == "Sushi" or fave_food == "sushi":
    print ("Ew, you like raw fish? What's wrong with you?")
elif fave_food == "burgers" or fave_food == "Burgers" or fave_food == "burger" or fave_food == "Burger":
    print ("Okay fatty. Tell you what, go on a run right now and I'll give you a Big Mac.")
else:
    # Create a list of possible responses
    print (f"{random_food_response}")

list_of_sport_responses = [
        "Yeah because I don't know what that is, it's irrelevant."
        "Alright bud."
        "Didn't ask."
        "Damn you boring as hell."
]
# Choose one of those responses randomly
random_sport_response = random.choice(list_of_sport_responses)

print(f"Okay, now what is your favourite sport? {user_name}")
fave_sport = input("That is if you even play any sports, looking at you I'm a bit doubtful. ")

if fave_sport == "Soccer" or fave_sport == "soccer":
    print ("You like to kick balls huh? I know your feet stink all the time.")
elif fave_sport == "Basketball" or fave_sport == "basketball":
    print ("Basketball or sitting on the bench watching others play basketball? No way YOU get any play time lmao.")
elif fave_sport == "Boxing":
    print ("Boxing huh? That's cool, not going to lie I'd knock you out with one hand easily.")
elif fave_sport == "Football" or fave_sport == "football" or fave_sport == "American football" or fave_sport == "american football":
    print ("Okay meathead. Didn't know you like getting concussions that much.")
elif fave_sport == "None" or fave_sport == "I don't have one" or fave_sport == "Don't have one" or fave_sport == "don't have one":
    print ("I figured. Go exersise you pathetic sap of unhealthiness.")
else:
    # Create a list of possible responses
    print (f"{random_sport_response}")