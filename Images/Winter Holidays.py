# Winter Holidays
# Author: Ethan
# 8 Janurary 2024

# Requirements: 
# - create a function called winter_holiday()
#    - takes one parameter - string
#    - returns a summary of a n event from your holidays

# Please do not use ChatGPT or any LLM

import random

def winter_holiday(good_or_bad: str) -> str:
    """Give a summary of our winter holiday 2023/24

    Params:
        good or bad - string that indicates whether the event 
            is good or bad
    
    Returns: 
        an event that happened to you during the holidays
        the event is selected part"""

winter_holiday = input("Type good to see a good event and vice versa. ")

random_good_events = ["I got to sleep a lot", "I bought myself a new game {lethal company}", "I got to hang out with my friends and play games all day"]
random_bad_events = ["I couldn't go ski because of bad weather", "I had to finish my uni applications", "I had to go back to school"]

if winter_holiday.strip().lower() == "good":
    print (random.choice(random_good_events))
elif winter_holiday.strip().lower() == "bad":
    print (random.choice(random_bad_events))
else:
    print ("Sorry, I only take good or bad events.")