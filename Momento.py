from copy import deepcopy

class Momento:
    def __init__(self, command, classCollection):
        self.command = command
        self.classCollection = classCollection
    def getState(self):
        return self.state
    def getCommand(self):
        return self.command
