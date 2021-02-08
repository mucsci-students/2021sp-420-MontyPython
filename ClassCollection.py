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
                print("Error: Name is already used") 
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
                print("Error: Class does not exist") 
                return

            for theTuple in self.relationshipDict.keys():
                if name in theTuple:
                    del self.relationshipDict[theTuple]
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
                print("Error: Old name does not exist") 
                return
            
            if newName in self.classDict:
                print("Error: New name is already used") 
                return

            self.classDict[newName] = self.classDict.pop(oldName)

            for theTuple in self.relationshipDict.keys():
                if oldName in theTuple:
                    (name1, name2) = theTuple
                    if name1 == oldName:
                        self.addRelationship(newName,name2)
                        self.deleteRelationship(oldName, name2)
                    else:
                        self.addRelationship(newName,name1)
                        self.deleteRelationship(oldName, name1)

            self.classDict.get(newName).rename(newName)

        # ------------------------ ( Relationship ) ------------------------- #

        def addRelationship(self, firstClassName, secondClassName):
            #Todo
            pass
        def deleteRelationship(self, firstClassName, secondClassName):
            #Todo
            pass

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
        
        # Used in unit tests
        # Returns all attributes that exist within the provided class
        def getAttributes(self, className):
            return self.classDict[className].getAttributes()