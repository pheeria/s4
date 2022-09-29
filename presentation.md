---
title: Introduction to Search Engines
author: Olzhas Askar
date: 2022-10-27
---

# But we have databases!

## Difficulties

```sql
SELECT * FROM restaurants
WHERE lower(name) LIKE '%halal%'
   OR lower(description) LIKE '%halal%'
   OR 'halal' IN tags
```

- difficult to write code which preserves the "meaning"
- difficult to use synonyms
- difficult to use stemming and lemmatization
- careless implementation may lead to whole table traversals

But! It's not impossible and Postgres provides with Full-Text Search capabilities!

## Search Engines

- implemented like NoSQL, preferring denormalization
- ease sharding/partitioning
- come with text analysis capabilities out of the box
- provide functionality for embedding synonyms and machine learning models

---

# What are we searching for?

To have it close to our domain, let's go with search for food.

- I tried to dog-food with foodpanda. It didn't quite fit the criteria.
- Tried UberEats as well. The same problem.
- Wolt gave me what I wanted.
- I didn't even consider Lieferando.

---

# Prepare the data

Let's grab a lot of restaurants!
Unfortunately, Germany isn't Taiwan, we don't have 3k+ restaurants at the same location.

```shell
# Restaurants in Berlin
curl "https://restaurant-api.wolt.com/v1/pages/restaurants?lat=52.516913793238444&lon=13.389984460880868" \
    | jq '.sections[1].items' > berlin.json

# Restaurants in Hamburg
curl "https://restaurant-api.wolt.com/v1/pages/restaurants?lat=53.5510846&lon=9.9936818" \
    | jq '.sections[1].items' > hamburg.json

# Restaurants in München
curl "https://restaurant-api.wolt.com/v1/pages/restaurants?lat=48.1351253&lon=11.5819806" \
    | jq '.sections[1].items' > münchen.json

# Restaurants in Köln
curl "https://restaurant-api.wolt.com/v1/pages/restaurants?lat=50.937531&lon=6.9602786" \
    | jq '.sections[1].items' > köln.json
```

--- 

# Combination

And now let's stitch it all together!

```shell
# Berlin + Hamburg + München + Köln = Germany
jq --slurp '[.[][]]' berlin.json hamburg.json münchen.json köln.json > germany.json
```


---

# TF-IDF

How to use a magic wand?

TF - term frequency
IDF - inverse document frequency

Stop words
to, a -> their IDF will be high anyways
