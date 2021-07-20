import json



def findPath(map, ST, END):
    explored = []
    queue = [[ST]]
    if ST == END:
        return "Same"
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            neighbours = map[node]
            for neighbour in neighbours:
                quickpass = list(path)
                quickpass.append(neighbour)
                queue.append(quickpass)
                 
                if neighbour == END:
                    print(quickpass)
                    return quickpass
            explored.append(node)
 
    
    print("No pass")
    return 0
 

mapdata = open("map.json","r")
 
verify = mapdata.readlines(-1)
mapdata.close()
if verify == "":
    pass
     

with open('map.json') as f:
  map = json.load(f)




findPath(map, 'A', 'H')