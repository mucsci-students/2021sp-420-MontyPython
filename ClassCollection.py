### File: ClassCollection.py
### Classes defined: ClassCollection

from Class import Class
from Relationship import Relationship
class ClassCollection():

        ## Initializes a ClassCollection Object 
        ## with a dictionary that will be filled
        ## with Classes
        ##
        ## Ex:   collection1 = ClassCollection()
        def __init__(self):         
            self.classDict = {}
            self.relationshipDict = {}

        # ---------------------------- ( Class ) ---------------------------- #
        
        ## Cast the user's name input to a string, creates
        ## a new dictionary entry for that name and assigns
        ## it the value of the class Object
        ##
        ## Ex:   collection1.addClass("ClassX")
        def addClass(self, name):
            if name in self.classDict:
                raise KeyError(f"{name} already exists")
            self.classDict[name] = Class(name)

        ## Cast the user's name input to a string, search 
        ## for the dictionary entry with that name, and remove
        ## that entry. Remove existing relationsips that contain 
        ## that class name.
        ##
        ## Ex:   collection1.deleteClass("ClassX")
        def deleteClass(self, name):
            if name not in self.classDict:
                raise KeyError(f"{name} does not exists")

            toDelete = []
            for theTuple in self.relationshipDict.keys():
                if name in theTuple:
                    toDelete.append(theTuple)
                               
            for temp in toDelete:
                del self.relationshipDict[temp]

            del self.classDict[name]     


        ## Cast the user's name input to a string, search 
        ## for the dictionary entry with that name. Pop &
        ## re-add the entry under the new name. Change the
        ## name of the class object. 
        ## Recreate or modify relationships involving that 
        ## class. Pending on how the relationships are 
        ## implemented.
        ##
        ## Ex:   collection1.renameClass("ClassX", "ClassY")
        def renameClass(self, oldName, newName):
            if oldName not in self.classDict:
                raise KeyError(f"{oldName} does not exist")
            
            if newName in self.classDict:
                raise KeyError(f"{newName} already exists")

            self.classDict[newName] = self.classDict[oldName]

            toChange = []
            typeList = []
            for theTuple, theType in self.relationshipDict.items():
                if oldName in theTuple:
                    toChange.append(theTuple)       
                    typeList.append(theType.typ)     
                               
            for theTuple, theType in zip(toChange, typeList):
                (name1, name2) = theTuple
                if name1 == oldName:
                    self.addRelationship(newName,name2, theType)
                    self.deleteRelationship(oldName, name2)
                else:
                    self.addRelationship(name1, newName, theType)
                    self.deleteRelationship(name1, oldName)

            self.classDict.pop(oldName)
            self.classDict.get(newName).rename(newName)

        # ------------------------ ( Relationship ) ------------------------- #

        def addRelationship(self, firstClassName, secondClassName, typ):
            # check if classes exist
            if firstClassName not in self.classDict:
                raise KeyError(f"{firstClassName} does not exist")
            
            if secondClassName not in self.classDict:
                raise KeyError(f"{secondClassName} does not exist")

            if (firstClassName, secondClassName) in self.relationshipDict:
                raise KeyError(f"Relationship, {firstClassName}, {secondClassName}, already exists")

            if typ not in ["aggregation", "composition", "inheritance", "realization"]:
                raise ValueError(f"Invalid Type: {typ}. Valid types are: aggregation, composition, inheritance, realization")

            self.relationshipDict[(firstClassName, secondClassName)] = Relationship(firstClassName, secondClassName, typ)
        
        def deleteRelationship(self, firstClassName, secondClassName):
            # check if classes exist
            if firstClassName not in self.classDict:
                raise KeyError(f"{firstClassName} does not exist")
            
            if secondClassName not in self.classDict:
                raise KeyError(f"{secondClassName} does not exist")

            if (firstClassName, secondClassName) not in self.relationshipDict:
                raise KeyError("Relationship does not exist")

            del self.relationshipDict[(firstClassName, secondClassName)]

        def renameRelationship(self, firstClassName, secondClassName, typ):
            # check if classes exist
            if firstClassName not in self.classDict:
                raise KeyError(f"{firstClassName} does not exist")
            
            if secondClassName not in self.classDict:
                raise KeyError(f"{secondClassName} does not exist")

            if (firstClassName, secondClassName) not in self.relationshipDict:
                raise KeyError(f"Relationship, {firstClassName}, {secondClassName}, does not exist")

            if typ not in ["aggregation", "composition", "inheritance", "realization"]:
                raise ValueError(f"Invalid Type: {typ}. Valid types are: aggregation, composition, inheritance, realization")

            self.relationshipDict[(firstClassName, secondClassName)].typ = typ
        
        # --------------------------- ( Method ) ----------------------------- #

        def addMethod(self, className, methodName, returnType, parameters = []):
            if className not in self.classDict:
                raise KeyError(f"{className} does not exist")
            self.classDict[className].addMethod(methodName, returnType, parameters)

        def deleteMethod(self, className, methodName, parameters):
            if className not in self.classDict:
                raise KeyError(f"{className} does not exist")
            self.classDict[className].deleteMethod(methodName, parameters)
        
        def renameMethod(self, className, methodName, parameters, newName):
            if className not in self.classDict:
                raise KeyError(f"{className} does not exist")
            self.classDict[className].renameMethod(methodName, parameters, newName)

        # --------------------------- ( Parameter ) ----------------------------- #
        # "parameters" is the parameter listt of the given method to distinguish it.
        def addParameter(self, className, methodName, parameters, typ, name):
            if className not in self.classDict:
                raise KeyError(f"{className} does not exist")
            self.classDict[className].addParameter(methodName, parameters, typ, name)

        def removeParameter(self, className, methodName, parameters, name):
            if className not in self.classDict:
                raise KeyError(f"{className} does not exist")
            self.classDict[className].removeParameter(methodName, parameters, name)

        def removeAllParameters(self, className, methodName, parameters):
            if className not in self.classDict:
                raise KeyError(f"{className} does not exist")
            self.classDict[className].removeAllParameters(methodName, parameters)

        def changeParameter(self, className, methodName, parameters, name, newType, newName):
            if className not in self.classDict:
                raise KeyError(f"{className} does not exist")
            self.classDict[className].changeParameter(methodName, parameters, name, newType, newName)
        
        def changeAllParameters(self, className, methodName, parameters, newParameters):
            if className not in self.classDict:
                raise KeyError(f"{className} does not exist")
            self.classDict[className].changeAllParameters(methodName, parameters, newParameters)
        
         # --------------------------- ( Field ) ----------------------------- #
         #error checking is done in Class.py
        def addField(self, className, name, dataType):
            if className not in self.classDict:
                raise KeyError(f"{className} does not exist")

            self.classDict[className].addField(name,dataType)

        def deleteField(self, className, name):
            if className not in self.classDict:
                raise KeyError(f"{className} does not exist")

            self.classDict[className].deleteField(name)
        
        def renameField(self, className, oldName, newName):
            if className not in self.classDict:
                raise KeyError(f"{className} does not exist")
                
            self.classDict[className].renameField(oldName,newName)

        def getField(self, className, name):
            if name not in self.classDict[className].fieldDict:
                raise KeyError(f'Error: Field {name} does not exist in {className}')
            return self.classDict[className].getField(name)

        # ---------------------- ( Coorodiantes ) ----------------------- #
        
        def getClassCoordinates(self, name):
            if name not in self.classDict:
                raise KeyError(f'Error: Class {name} does not exist')
            return (self.classDict[name].getX(), self.classDict[name].getY())

        def setClassCoordinates(self, name, X, Y):
            if name not in self.classDict:
                raise KeyError(f'Error: Class {name} does not exist')
            self.classDict[name].setX(X)
            self.classDict[name].setY(Y)
        
        # ---------------------- ( Helper Functions ) ----------------------- #

        # Used in unit tests
        # Returns if the provided name exists within classDict
        def getClass(self, name):
            if name not in self.classDict:
                raise KeyError(f'Error: Class {name} does not exist')

            return self.classDict[name]

        def getRelationship(self, firstClassName, secondClassName):
            if (firstClassName, secondClassName) not in self.relationshipDict:
                raise KeyError(f'Error: relationship, {firstClassName}, {secondClassName} does not exist')
            
            return self.relationshipDict[(firstClassName, secondClassName)]

        # Used in REPL to direct user to a specific method of a given name
        # Returns a list of all methods under said given name
        def getMethodsByName(self, className, methodName):
            if className not in self.classDict:
                raise KeyError(f'Error: Class {className} does not exist')
            if methodName not in self.classDict[className].methodDict:
                raise KeyError(f'Error: No method {methodName} in {className} exists')

            return self.classDict[className].methodDict[methodName]

        def getMethod(self, className, methodName, overloadIndex):
            if className not in self.classDict:
                raise KeyError(f'Error: Class {className} does not exist')
            if methodName not in self.classDict[className].methodDict:
                raise KeyError(f'Error: No method {methodName} in {className} exists')

            return self.classDict[className].methodDict[methodName][overloadIndex]
        
        def getAllMethods(self, className):
            if className not in self.classDict:
                raise KeyError(f'Error: Class {className} does not exist')

            return self.classDict[className].methodDict
        
        def getFields(self, className):
            if className not in self.classDict:
                raise KeyError(f'Error: Class {className} does not exist')
            return self.classDict[className].fieldDict
        
