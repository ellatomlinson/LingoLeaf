import random

# Get a random practice sentence from practice_phrases.csv
def get_random_phrase():
    with open("data/practice_phrases.csv", "r") as file:
        lines = [line.strip() for line in file if line.strip()]
    print(random.choice(lines))

get_random_phrase()