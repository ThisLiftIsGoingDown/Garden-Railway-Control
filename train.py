import PathFinder



class Train:
    def __init__(self, id, startPosition):
        self.id = id
        self.position = startPosition
    
    def getId(self):
        return self.id
    
    def setId(self, newId):
        self.id = newId

    def setDestination(self, destination):
        self.destination = destination
        self.route = PathFinder.findPath(PathFinder.map, self.position, destination)
        