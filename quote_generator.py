import random

_QUOTES = [
    "Stay hungry, stay foolish.",
    "Discipline equals freedom.",
    "Make it work. Make it right. Make it fast.",
]

def get_random_quote():
    return random.choice(_QUOTES)

if __name__ == "__main__":
    print(get_random_quote())
