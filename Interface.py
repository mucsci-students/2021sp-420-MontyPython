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


#{
# (classA, classB) : relationship is currently ""
# }
#]

#[
#    {
#    "classA" :
#       [
#           {
#           "fieldA" : type
#           } 
#           {
#           "methodA" : 
#               [
#               (type, [params])
#               (type, [params])
#               ]
#           }
#       ]
#    }
#    {
#    (classA, classB) : type
#    } 
#]

### Save
def saveFile(collection, fileName=None):
    #Value Error if no file name is given
    if fileName == None:
        raise ValueError("No file name given to save")

    nameList = []
    methodsList = []
    fieldsList = []

    for classObj in collection.classDict.values():
        nameList.append(classObj.name)
        methodsList.append(classObj.methodDict)
        fieldsList.append(classObj.fieldDict)

    classesDictionary = {}

    for name, methodDict, fieldDict in zip(nameList, methodsList, fieldsList):
        methodsDictionary = {}
        fieldsDictionary = {}

        for methodName, methodVariants in methodDict.items():
            variantList = []

            for each in methodVariants:
                variantList.append((each.returnType, each.parameters))

            methodsDictionary[methodName] = variantList

        for fieldName, fieldType in fieldDict.items():
            fieldsDictionary[fieldName] = fieldType.dataType

        classesDictionary[name] = (methodsDictionary, fieldsDictionary)

    relationshipsDictionary = {}
    #When saving to JSON, a tuple cannot be used as a key. The tuple
    #is saved as a string, delimited by ", ".
    #A dictionary is formed with the string as the key
    for key, value in collection.relationshipDict.items():
        stringKey = ', '.join(str(s) for s in key)  
        relationshipsDictionary[stringKey] = value.typ

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

        #Creates a class class for each entry in the classes dictionary
        #Within each class, creates an attribute class for each attribute
        #entry in the attributes dictionary
        for name, methodField in classesDictionary.items():
            collection.addClass(name)
            
            methodsDictionary = methodField[0]
            fieldsDictionary = methodField[1]

            for field, typ in fieldsDictionary.items():
                collection.addField(name, field, typ)

            for method, variantList in methodsDictionary.items():
                for variant in variantList:
                    collection.addMethod(name, method, variant[0], variant[1])

        #Reforms relationship dictionary, creating a tuple from
        #the string delimited by ", "
        for key, value in relationshipsDictionary.items():
            classes = key.split(", ")
            collection.addRelationship(classes[0], classes[1], value)
        
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
