import json
import sys
### Interface.py

### List classes
def listClasses(collection):
    #todo
    pass

### List class
def listClass(collection, name):
    #todo
    pass

### List relationships
def listRelationships(collection):
    #todo
    pass

### Save
        # name list = class.name for class in classDict
        # attributes list = class.attributeDict for class in classDict
        # for name, attr in zip(name list, attributes list):
        #       outputClassDict[name] = attr
        # relationships list = classcollection.relationshipDict
def saveFile(collection, fileName):
    nameList = []
    attributesList = []
    for classObj in collection.classDict.values():
        nameList.append(classObj.name)
        attributesList.append(classObj.attributeDict)

    classesDictionary = {}
    for name, attributes in zip(nameList, attributesList):
        classesDictionary[name] = attributes

    relationshipsDictionary = {}
    for key, value in collection.relationshipDict.items():
        stringKey = ', '.join(str(s) for s in key)
        relationshipsDictionary[stringKey] = value

    classesRelationshipsList = [classesDictionary, relationshipsDictionary]

    fileName += ".monty"
    with open(fileName, "w") as f:
        json.dump(classesRelationshipsList, f)
    

### Load
def loadFile(collection, fileName):
    collection.classDict = {}
    collection.relationshipDict = {}
    classesRelationshipsList = []
    fileName += ".monty"
    with open(fileName, "r") as f:
        classesRelationshipsList = json.load(f)

    classesDictionary = classesRelationshipsList[0]
    relationshipsDictionary = classesRelationshipsList[1]

    for key, value in relationshipsDictionary.items():
        tupleKey = tuple(key.split(", "))
        collection.relationshipDict[tupleKey] = value

    for name, attributes in classesDictionary.items():
        collection.addClass(name)
        collection[name].attributeDict = attributes
        
        
### Help
def help():
    pass

### Exit
def exit():
    sys.exit()