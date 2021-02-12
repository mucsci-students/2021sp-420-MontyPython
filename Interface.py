import json
import sys
import os
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
def saveFile(collection, fileName=None):
    #Value Error if no file name is given
    if fileName == None:
        raise ValueError("No file name given to save")

    nameList = []
    attributesList = []
    #Iterates through collection
    #Enters a class's name field into nameList
    #Enters a class's attributes dictionary field into attributesList
    for classObj in collection.classDict.values():
        nameList.append(classObj.name)
        attributesList.append(classObj.attributeDict)

    classesDictionary = {}
    #Iterates through nameList and attributesList
    #zip() ends when the shorter of two lists is emptied
    #The assumption is made that there will never be a class that
    #does not have both a name and an attributes dictioanry field.
    #Forms a dictionary of classes with a key of name and a value of
    #the attributes dictionary
    for name, attributesDict in zip(nameList, attributesList):
        attributesDictionary = {}
        #attributeValue is an attribute object
        #As currently implemented, attribute objects only contain
        #the name of the attribute, and so that is the value pulled.
        for attributeName in attributesDict:
            attributesDictionary[attributeName] = attributeName
        classesDictionary[name] = attributesDictionary

    relationshipsDictionary = {}
    #When saving to JSON, a tuple cannot be used as a key. The tuple
    #is saved as a string, delimited by ", ".
    #A dictionary is formed with the string as the key
    for key, value in collection.relationshipDict.items():
        stringKey = ', '.join(str(s) for s in key)
        relationshipsDictionary[stringKey] = value

    #The classes dictionary and the relationships dictionary are
    #formed into a list, allowing for a singular structure to be dumped
    classesRelationshipsList = [classesDictionary, relationshipsDictionary]

    #Adds file extension
    fileName += ".monty"
    #Dumps classes and relationships list to file
    with open(fileName, "w") as f:
        json.dump(classesRelationshipsList, f)
    

### Load
def loadFile(collection, fileName=None):
    #When no file name is supplied by the user, raises a Value Error
    if fileName == None:
        raise ValueError("No file name given to load")
    #Adds file extension
    fileName += ".monty"
    #Check for file existence
    #Makes assumption that a file of extension .monty has the same
    #structure as created by the save function
    if os.path.isfile(fileName):
        collection.classDict = {}
        collection.relationshipDict = {}
        classesRelationshipsList = []
        
        #File loading
        with open(fileName, "r") as f:
            classesRelationshipsList = json.load(f)

        #Splits classes and relationships list into the component
        #dictionaries
        classesDictionary = classesRelationshipsList[0]
        relationshipsDictionary = classesRelationshipsList[1]

        #Reforms relationship dictionary, creating a tuple from
        #the string delimited by ", "
        for key, value in relationshipsDictionary.items():
            tupleKey = tuple(key.split(", "))
            collection.relationshipDict[tupleKey] = value

        #Creates a class class for each entry in the classes dictionary
        #Within each class, creates an attribute class for each attribute
        #entry in the attributes dictionary
        for name, attributes in classesDictionary.items():
            collection.addClass(name)
            for attribute in attributes.keys():
                collection[name].addAttribute(attribute)
        
    #Raises an OS Error if the file does not exist
    else:
        raise OSError("No file of given name found")
        
### Help
def help():
    with open('Help.txt') as helpFile:
        helpText = helpFile.read()
    print(helpText)

### Exit
def exit():
    sys.exit()