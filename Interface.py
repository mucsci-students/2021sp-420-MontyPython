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

def saveFile(collection, fileName=None, GUI="CLI", mainWindow=None):
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
    linesDictionary = {}
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
            oldClassesRelationshipsCoordsLinesList = json.load(f)
            try:
                coordsDictionary = oldClassesRelationshipsCoordsLinesList[2]
            except IndexError:
                coordsDictionary = {}
            try: 
                linesDictionary = oldClassesRelationshipsCoordsLinesList[3]
            except IndexError:
                linesDictionary = {}

        #Logic for updating class coordinates from existing file
        #If class was removed, pops coords from coordsDictionary
        #If class was added, defaults coords for that class to (-1, -1)
        coordsDictionaryReplica = coordsDictionary.copy()
        for key in coordsDictionary.keys():
            if key not in classesDictionary.keys():
                coordsDictionaryReplica.pop(key)
        for key in classesDictionary.keys():
            if key not in coordsDictionary.keys():
                coordsDictionaryReplica[key] = (-1, -1)
        coordsDictionary = coordsDictionaryReplica

        #Logic for updating line coordinates from existing file
        #If relationship was removed, pops coords from linesDictionary
        #If relationship was added, default coords are (-1, -1, -1, -1)
        #Type is pulled from relationship dictionary
        linesDictionaryReplica = linesDictionary.copy()
        for key in linesDictionary.keys():
            if key not in relationshipsDictionary.keys():
                linesDictionaryReplica.pop(key)
        for key, relationType in relationshipsDictionary.items():
            if key not in linesDictionary.keys():
                #Automatically finds coords for each class in a relationship
                #Supplies those coordinates to linesDictionary
                #Exception handling failsafes to (-1, -1, -1, -1)
                classes = classesString.split(", ")
                try:
                    FirstX, FirstY = coordsDictionary[classes[0]]
                except ValueError:
                    FirstX, FirstY = (-1, -1)
                try:
                    SecondX, SecondY = coordsDictionary[classes[1]]
                except ValueError:
                    SecondX, SecondY = (-1, -1)

                linesDictionaryReplica[key] = (FirstX, FirstY, SecondX, SecondY, relationType)
        linesDictionary = linesDictionaryReplica

    #If file does not exist and save is invoked in the CLI,
    #all class coords are set to the default of (-1, -1)
    elif not priorExistence and GUI.lower() != "gui":
        for key in classesDictionary.keys():
            coordsDictionary[key] = (-1, -1)
        
        for classesString, relationType in relationshipsDictionary.items():
            linesDictionary[classesString] = (-1, -1, -1, -1, relationType)

    #Regardless of file existence, if save is invoked in the GUI,
    #uses the mainWindow object (which is required if saving in the GUI)
    #to add/overwrite the coordinate list via the MainWindow object's classDict
    #Does the same for the line dictionary's coordinates
    else:
        #temp defaulting until coord dictionary is decided upon
        #different default value for testing
        for key, obj in mainWindow.classDict.items():
            coordsDictionary[key] = (obj.x, obj.y)
        #Uncomment, changed to proper formatting once GUI coordinates are ironed out
        #coordsDictionary = coords
        for classesTuple, lineCoords in mainWindow.lineDict.items():
            classesString = ', '.join(str(s) for s in key)  
            linesDictionary[classesString] = lineCoords

    #classesDictionary, relationshipsDicttionary, and coordsDictionary are
    #formed into a list to be json dumped to the supplied file
    classesRelationshipsCoordsLinesList = [classesDictionary, relationshipsDictionary, coordsDictionary, linesDictionary]

    with open(fileName, "w") as f:
        json.dump(classesRelationshipsCoordsLinesList, f)

### Load
def loadFile(collection, fileName=None, GUI="CLI", mainWindow=None):
    #When no file name is supplied by the user, raises a Value Error
    if fileName == None:
        raise ValueError("No file name given to load")

    if mainWindow == None and GUI.lower() == "gui":
        raise ValueError("No coordinates dictionary given")
    
    #Adds file extension if not already included
    if not fileName.endswith(".monty"):
        fileName += ".monty"

    #Check for file existence
    #Makes assumption that a file of extension .monty has the same
    #structure as created by the save function
    if os.path.isfile(fileName):
        collection.classDict = {}
        collection.relationshipDict = {}
        classesRelationshipsCoordsLinesList = []
        
        #File loading
        with open(fileName, "r") as f:
            classesRelationshipsCoordsLinesList = json.load(f)

        #Splits classes,relationships, and coords dictionarys
        #from the inputed list
        try:
            classesDictionary = classesRelationshipsCoordsLinesList[0]
        except IndexError:
            classesDictionary = {}
        try:
            relationshipsDictionary = classesRelationshipsCoordsLinesList[1]
        except IndexError:
            relationshipsDictionary = {}
        try:
            coordsDictionary = classesRelationshipsCoordsLinesList[2]
        except IndexError:
            coordsDictionary = {}

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
        if GUI.lower() == "gui" and coords != None:
            for name, loc in coordsDictionary.items():
                coords[name] = loc
        
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
