import sys
from ClassCollection import ClassCollection
from PyQt5.QtWidgets import QLabel

# A default collection
collection = ClassCollection()

class GUIController:
    def __init__(self, model):
        self.model = model
    
    def open(self):
        pass

    def save(self):
        pass

    def help(self):
        pass

    def exit(self):
        sys.exit()

    def addClass(self, name):
        pass
        # Take the info from the addClass menu, store in the classcollection and find a way to display it on the main window

    def deleteClass(self, name):
        pass
        # Take the name of the class from the menu, update the classcollection, and delete the class from the main window

    def renameClass(self, oldName, newName):
        pass

    def addRelationship(self, firstClassName, secondClassName, typ):
        pass

    def deleteRelationship(self, firstClassName, secondClassName):
        pass

    def renameRelationship(self, firstClassName, secondClassName, typ):
        pass

    def addMethod(self, className, methodName, returnType, parameters):
        pass

    def deleteMethod(self, className, methodName):
        pass

    def renameMethod(self, className, methodName, newName):
        pass

    def addParameter(self, className, methodName, typ, name):
        pass

    def removeParameter(self, className, methodName, name):
        pass

    def changeParameter(self, className, methodName, name, newType, newName):
        pass

    def addField(self, className, name, dataType):
        pass

    def deleteField(self, className, name):
        pass

    def renameField(self, className, oldName, newName):
        pass


# Create a method to pull info about classes from a class collection instance. Maybe that should be made here?
# This may end up being similar to interface.py and REPL.py
