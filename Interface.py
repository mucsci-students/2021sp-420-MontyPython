import json
import sys
### Interface.py

### List classes
def listClasses(collection):
    for currentClass in collection.classDict:
        listClass(collection, currentClass)

### List class
def listClass(collection, name):
    # check if class exists in the collection
    if name not in collection.classDict:
        raise KeyError(f"Class {name} not found")

    print(f"-{name}")
    for attr in collection.classDict[name].attributeDict:
        print(f"\t* {attr}")

### List relationships
def listRelationships(collection):
    for relationship in collection.relationshipDict:
        print(f"\t{relationship[0]} -> {relationship[1]}")

### Save
        # name list = class.name for class in classDict
        # attributes list = class.attributeDict for class in classDict
        # for name, attr in zip(name list, attributes list):
        #       outputClassDict[name] = attr
        # relationships list = classcollection.relationshipDict
def saveFile(collection, fileName):
    pass
    

### Load
def loadFile(collection, fileName):
    pass
        
        
### Help
def help():
    with open('Help.txt') as helpFile:
        helpText = helpFile.read()
    print(helpText)

### Exit
def exit():
    sys.exit()
