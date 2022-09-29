from utils import load_file, save_file, tokenize

documents = load_file("./germany.json")

index = {
    "indices": {
        "name": {},
        "short_description": {},
        "tags": {},
    },
    "source": {}
}


def populate(store: dict, tokens: list, source_index: int) -> None:
    for token in tokens:
        if token not in store:
            store[token] = []
        store[token].append(i)


for i, document in enumerate(documents):
    index["source"][i] = document
    
    restaurant = document["venue"]
    populate(index["indices"]["name"], tokenize(restaurant["name"]), i)
    populate(index["indices"]["short_description"], tokenize(restaurant["short_description"]), i)
    populate(index["indices"]["tags"], restaurant["tags"], i)


save_file("./s4.json", index)
