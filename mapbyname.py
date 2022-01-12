map_by_name = lambda arr : list(map(lambda x: x["name"], arr))  

pets = [
  {"type":"dog", "name":"Rolo"},
  {"type":"cat", "name":"Sunny"},
  {"type":"rat", "name":"Saki"},
  {"type":"dog", "name":"Finn"},
  {"type":"cat", "name":"Buffy"}
]
print(map_by_name(pets)) #: ["Rolo", "Sunny", "Saki", "Finn", "Buffy"]

countries = [
 {"name":"Japan", "continent":"Asia"},
 {"name":"Hungary", "continent":"Europe"},
 {"name":"Kenya", "continent":"Africa"},
]
print(map_by_name(countries)) #: ["Japan", "Hungary", "Kenya"]
