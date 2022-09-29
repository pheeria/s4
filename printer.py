import json

def pretty_print(restaurant):
    print(restaurant["name"])
    cuisines = [c["name"] for c in restaurant["cuisines"]]
    print(", ".join(cuisines))
    print(f"{restaurant['rating']}/5 out of {restaurant['review_number']} reviews")

with open("./sg.json") as file:
    restaurants = json.loads(file.read())
    for each in restaurants:
        pretty_print(each)
        print("-- -- --")

