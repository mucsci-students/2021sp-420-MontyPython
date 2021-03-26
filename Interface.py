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
#    {
#    "class A" : (X coord, Y coord)
#    "class B" : (X coord, Y coord)
#    }
#]

### Save

#collection is a required parameter, referring to a ClassCollection object to save

#fileName is a required parameter, referring to the file/path to save to.
#   fileName's default value of None is used for failsafe error handling

#GUI is an optional parameter, referring to save being invoked in the CLI vs GUI
#   this defaults to saving in the CLI
#   when saving in the GUI, mainWindow becomes required
#   used for handling the dictionary of classes to their coordinate values
#   set the string to "GUI" to save in GUI, this is case insensitive

#coords is an optional parameter, referring to a coordinate dictionary in the GUI
#   becomes required if GUI = "GUI" (case insensitive)
#   currently unused, GUI coordinates aren't set for sure yet.

def saveFile(collection, fileName=None, GUI="CLI", coords=None):
    #Value Error if no file name is given
    if fileName == None or fileName.endswith("\\"):
        raise ValueError("No file name given to save")

    #Adds file extension if not already included
    if not fileName.endswith(".monty"):
        fileName += ".monty"

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
    
    coordsDictionary = {}
    #If file already exists, pulls coordinates from loading the file
    #Downside: not backwards compatible with old saved files
    #Upside: easily preserves coordinates when editing in the CLI without
    #having to have direct access or even have instances of the GUI classes open
    priorExistence = os.path.exists(fileName)

    #If file already exists and save is invoked in the CLI, loads file to find
    #already present coordinates. Handles checks for added/deleted classes
    #since the last save. Any class added in the CLI will have coords set to (-1, -1)
    if priorExistence and GUI.lower() != "gui":
        with open(fileName, "r") as f:
            oldClassesRelationshipsCoordsList = json.load(f)
            coordsDictionary = oldClassesRelationshipsCoordsList[2]

        #Logic for updating class coordinates from existing file
        #If class was removed, pops coords from coordsDictionary
        #If class was added, defaults coords for that class to (-1, -1)
        for key in coordsDictionary.keys():
            if key not in classesDictionary.keys():
                coordsDictionary.pop(key)
        for key in classesDictionary.keys():
            if key not in coordsDictionary.keys():
                coordsDictionary[key] = (-1, -1)

    #If file does not exist and save is invoked in the CLI,
    #all class coords are set to the default of (-1, -1)
    elif not priorExistence and GUI.lower() != "gui":
        for key in classesDictionary.keys():
            coordsDictionary[key] = (-1, -1)

    #Regardless of file existence, if save is invoked in the GUI,
    #uses the mainWindow object (which is required if saving in the GUI)
    #to add/overwrite the coordinate list via the MainWindow object's classDict
    else:
        #temp defaulting until coord dictionary is decided upon
        #different default value for testing
        for key in classesDictionary.keys():
            coordsDictionary[key] = (-2, -2)
        #Uncomment, changed to proper formatting once GUI coordinates are ironed out
        #coordsDictionary = coords

    #classesDictionary, relationshipsDicttionary, and coordsDictionary are
    #formed into a list to be json dumped to the supplied file
    classesRelationshipsCoordsList = [classesDictionary, relationshipsDictionary, coordsDictionary]

    with open(fileName, "w") as f:
        json.dump(classesRelationshipsCoordsList, f)

### Load
def loadFile(collection, fileName=None):
    #When no file name is supplied by the user, raises a Value Error
    if fileName == None:
        raise ValueError("No file name given to load")
    
    #Adds file extension if not already included
    if not fileName.endswith(".monty"):
        fileName += ".monty"

    #Check for file existence
    #Makes assumption that a file of extension .monty has the same
    #structure as created by the save function
    if os.path.isfile(fileName):
        collection.classDict = {}
        collection.relationshipDict = {}
        classesRelationshipsCoordsList = []
        
        #File loading
        with open(fileName, "r") as f:
            classesRelationshipsCoordsList = json.load(f)

        #Splits classes,relationships, and coords dictionarys
        #from the inputed list
        classesDictionary = classesRelationshipsCoordsList[0]
        relationshipsDictionary = classesRelationshipsCoordsList[1]
        coordsDictionary = classesRelationshipsCoordsList[2]

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

        #Skeleton for coordinate dictionary when that gets settled in the GUI
        for key, value in coordsDictionary.items():
            pass
        
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
