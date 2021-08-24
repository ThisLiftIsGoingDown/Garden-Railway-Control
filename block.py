from enum import Enum

class State(Enum):
    vacant = 0
    occupied = 1
    outOfService = 2

class Block:
    def __init__(self, node , startState = State.vacant):
        self.node = node
        self.state = startState
    
    def checkState(self):
        return self.state

    def updateState(self, newState):
        self.state = newState


