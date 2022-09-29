from time import time

from utils import load_file, pretty_print

restaurants = load_file("./germany.json")

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
        pretty_print(restaurant)

