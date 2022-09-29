import re
import json
from unicodedata import normalize


def pretty_print(restaurant: dict):
    venue = restaurant["venue"]
    cuisines = ", ".join(venue["tags"])
    rating = venue["rating"]["score"] if "rating" in venue else 0
    print(venue["name"])
    print(venue["short_description"])
    print(f"Rating: {rating}, Tags: {cuisines}")
    print()


def tokenize(text: str) -> list: 
    return [normalize("NFKD", token).encode("ASCII", "ignore").decode("ASCII")
            for token in re.split(r"\W+", text.lower())]


def load_file(filename: str):
    with open(filename) as file:
        return json.loads(file.read())


def save_file(filename: str, content):
    with open(filename, "w") as file:
        file.write(json.dumps(content, indent=4))

