import Export
class Node:
    def __init__(self, id, neighbours = []) -> None:
        self.id = id
        self.neighbours = neighbours

class Map:
    def __init__(self) -> None:
        self.map = []
    
    def findPath(start, end):
        pass

    def loadMap(self):
        self.map = Export.Exporter.importMap()