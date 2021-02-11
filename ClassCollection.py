### File: ClassCollection.py
### Classes defined: ClassCollection

from Class import Class

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
                print(f"Error: {name} already exists")
                return
            self.classDict[name] = Class(name)

        ## Cast the user's name input to a string, search 
        ## for the dictionary entry with that name, and remove
        ## that entry. Remove existing relationsips that contain 
        ## that class name.
        ##
        ## Ex:   collection1.deleteClass("ClassX")
        def deleteClass(self, name):
            if name not in self.classDict:
                print(f"Error: {name} does not exist")
                return

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
                print(f"Error: {oldName} does not exist") 
                return
            
            if newName in self.classDict:
                print(f"Error: {newName} is already used")
                return

            self.classDict[newName] = self.classDict.pop(oldName)
            toChange = []
            for theTuple in self.relationshipDict.keys():
                if oldName in theTuple:
                    toChange.append(theTuple)            
                               
            for theTuple in toChange:
                (name1, name2) = theTuple
                if name1 == oldName:
                    self.addRelationship(newName,name2)
                    self.deleteRelationship(oldName, name2)
                else:
                    self.addRelationship(name1, newName)
                    self.deleteRelationship(name1, oldName)


            self.classDict.get(newName).rename(newName)

        # ------------------------ ( Relationship ) ------------------------- #

        def addRelationship(self, firstClassName, secondClassName):
            # check if classes exist
            if firstClassName not in self.classDict:
                raise KeyError(f"{firstClassName} does not exist")
            
            if secondClassName not in self.classDict:
                raise KeyError(f"{secondClassName} does not exist")

            if (firstClassName, secondClassName) in self.relationshipDict:
                raise KeyError(f"Relationship, {firstClassName}, {secondClassName}, already exists")

            self.relationshipDict[(firstClassName, secondClassName)] = ""
        
        def deleteRelationship(self, firstClassName, secondClassName):
            # check if classes exist
            if firstClassName not in self.classDict:
                raise KeyError(f"{firstClassName} does not exist")
            
            if secondClassName not in self.classDict:
                raise KeyError(f"{secondClassName} does not exist")

            del self.relationshipDict[(firstClassName, secondClassName)]

        # -------------------------- ( Attribute ) -------------------------- #
        ## Wrapper functions for dealing with attributes of a specific class.

        def addAttribute(self, className, attributeName):
            self.classDict[className].addAttribute(attributeName)

        def deleteAttribute(self, className, attributeName):
            self.classDict[className].deleteAttribute(attributeName)

        def renameAttribute(self, className, oldAttributeName, newAttributeName):
            self.classDict[className].renameAttribute(oldAttributeName, newAttributeName)
        
        # ---------------------- ( Helper Functions ) ----------------------- #

        # Used in unit tests
        # Returns if the provided name exists within classDict
        def getClass(self, name):
            if name not in self.classDict:
                print(f"Error: {name} does not exist")
                return None

            return self.classDict[name]
        
        def getAttribute(self, className, attributeName):
            return self.classDict[className].getAttribute(attributeName)

        # Used in unit tests
        # Returns all attributes that exist within the provided class
        def getAttributes(self, className):
            return self.classDict[className].getAttributes()

        def getRelationship(self, firstClassName, secondClassName):
            if (firstClassName, secondClassName) not in self.relationshipDict:
                print(f"Error: relationship, {firstClassName}, {secondClassName} does not exist")
                return None
            
            return self.relationshipDict[(firstClassName, secondClassName)]
