import pickle
class Exporter:
    def exportMap(data):
        pickle.dump(data, open("main.map", "wb"))
    
    def importMap():
        return pickle.load(open("main.map", "rb"))
    
    def exportTrains(data):
        pickle.dump(data, open("main.trains", "wb"))
    
    def importTrains():
        return pickle.load(open("main.trains", "rb"))