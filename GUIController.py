import sys
from ClassCollection import ClassCollection
from PyQt5.QtWidgets import QLabel

# A default collection
collection = ClassCollection()


def open():
    pass

def save():
    pass

def help():
    pass

def exit():
    sys.exit()

def addClass(name):
    pass
    # Take the info from the addClass menu, store in the classcollection and find a way to display it on the main window

def deleteClass(name):
    pass
    # Take the name of the class from the menu, update the classcollection, and delete the class from the main window

def renameClass(oldName, newName):
    pass

def addRelationship(firstClassName, secondClassName, typ):
    pass

def deleteRelationship(firstClassName, secondClassName):
    pass

def renameRelationship(firstClassName, secondClassName, typ):
    pass

def addMethod(className, methodName, returnType, parameters = []):
    pass

def deleteMethod(self, className, methodName):
    pass

def renameMethod(className, methodName, newName):
    pass

def addParameter(className, methodName, typ, name):
    pass

def removeParameter(className, methodName, name):
    pass

def changeParameter(className, methodName, name, newType, newName):
    pass

def addField(className, name, dataType):
    pass

def deleteField(className, name):
    pass

def renameField(className, oldName, newName):
    pass


# Create a method to pull info about classes from a class collection instance. Maybe that should be made here?
# This may end up being similar to interface.py and REPL.py
