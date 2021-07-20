"""This is a simple tool to create the map.json file 
for path finding."""

import json
"""Insert your map here as Python Dictonary"""
map = { "A" : ["B","C"],
    "B" : ["A","D"],
    "C" : ["A"]
}

with open('map.json') as f:
  mapOld = json.load(f)

print(f"do you really want to override this map:\n{mapOld}\nWith this One:\n{map} ?\n(y/n)")
tmp = input()
tmp = tmp.lower()

if tmp == "y":

    with open("map.json", "w") as write_file:
        json.dump(map, write_file)


    with open('map.json') as f:
        mapCh = json.load(f)


    print(f"The Following Map has been Saved in 'map.json': {mapCh} ")
else:
    print("Action Canceled")