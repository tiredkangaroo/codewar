def map_by_key(arr, key):
    return list(map(lambda x: x[key], arr))

locations = [
  {"city":"New York City", "state":"New York", "coast":"East"},
  {"city":"San Francisco", "state":"California", "coast":"West"},
  {"city":"Portland", "state":"Oregon", "coast":"West"},
]

print(map_by_key(locations, "state")) #: ["New York", "California", "Oregon"]
print(map_by_key(locations, "city")) #: ["New York City", "San Francisco", "Portland"]