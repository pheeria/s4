import re
import json
from unicodedata import normalize


def pretty_print(restaurant: dict):
    cuisines = ", ".join(restaurant["tags"])
    print(f"{restaurant['name']}")
    print(restaurant["short_description"])
    print(f"Rating: {restaurant['rating']['score']}, Tags: {cuisines}")
    print()


def tokenize(text: str) -> list: 
    return [normalize("NFKD", token).encode("ASCII", "ignore").decode("ASCII")
            for token in re.split(r"\W+", text.lower())]


def load(filename: str):
    result = None
    with open(filename) as file:
        result = json.loads(file.read())
    return result