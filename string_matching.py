import json
from time import time

restaurants = []
with open("./germany.json") as file:
    restaurants = json.loads(file.read())

while True:
    search_results = []
    query = input("Enter your search query: ")

    start = time()

    for each in restaurants:
        restaurant = each["venue"]
        if (query in restaurant["name"]
            or query in restaurant["short_description"]
            or query in restaurant["tags"]):
            search_results.append(restaurant)

    end = time()

    print(f"Found {len(search_results)} results out of total {len(restaurants)} in {(end - start) * 1000:.2f}μs")
    print("-- -- -- --")

    for restaurant in search_results[:3]:
        cuisines = ", ".join(restaurant["tags"])
        print(f"{restaurant['name']}")
        print(restaurant["short_description"])
        print(f"Rating: {restaurant['rating']['score']}, Tags: {cuisines}")
        print()



