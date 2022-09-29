from time import time
from utils import load_file, pretty_print, tokenize

store = load_file("./s4.json")

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

    print(f"Found {len(search_results)} results out of total {len(store['source'])} in {(end - start) * 1000:.2f}μs")
    print("-- -- -- --")

    print(search_results)
    for doc_id in search_results[:3]:
        pretty_print(store["source"][str(doc_id)])



