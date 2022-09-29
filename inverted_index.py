from time import time
from utils import load, pretty_print, tokenize

store = load("./s4.json")

while True:
    search_results = []
    query = input("Enter your search query: ")

    start = time()

    tokens = tokenize(query)

    for index in store["indices"].values():
        for token in tokens:
            if token in index:
                search_results.extend(index[token])

    end = time()

    print(f"Found {len(search_results)} results out of total {len(store)} in {(end - start) * 1000:.2f}μs")
    print("-- -- -- --")

    print(search_results)
    # for restaurant in search_results[:3]:
    #     pretty_print(restaurant)


