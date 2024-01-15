# Comparing Similarity Scores
# Author: Ubial
# 8 November 2023

# Calculate similairty scores between two people
# Create two lists that represent the movies
# that people like
tim_favourite_movies = [
    "Pacific Rim",
    "Advengers Infinity War",
    "Lilo and Stitch",
    "The little Prince",
    "Spiderman Across the Spider Verse" ]

bob_favourite_movies = [
    "Spiderman Across the Spider verse", 
    "Howl's moving castle",
    "Pacific Rim",
    "Ponyo" ]

ethan_favourite_movies = [
    "Spiderman Across the Spider Verse",
    "Howl's moving castle",
    "Cowboy bebop movie"]

# Initialize the simiarity score

similarity_score = 0

# Iterate through all movies in first list
for movies in ethan_favourite_movies:
    if movies in tim_favourite_movies:
        similarity_score += 1