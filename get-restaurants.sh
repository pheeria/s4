# Restaurants in Hamburg
curl "https://restaurant-api.wolt.com/v1/pages/restaurants?lat=53.5510846&lon=9.9936818" \
    | jq '.sections[1].items' > hamburg.json

# Restaurants in München
curl "https://restaurant-api.wolt.com/v1/pages/restaurants?lat=48.1351253&lon=11.5819806" \
    | jq '.sections[1].items' > münchen.json

# Restaurants in Köln
curl "https://restaurant-api.wolt.com/v1/pages/restaurants?lat=50.937531&lon=6.9602786" \
    | jq '.sections[1].items' > köln.json

