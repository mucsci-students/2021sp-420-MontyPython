### File: ClassCollection.py
### Classes defined: ClassCollection

import Class

class ClassCollection():

        ## Initializes a ClassCollection Object 
        ## with a dictionary that will be filled
        ## with Classes
        ##
        ## Ex:   collection1 = ClassCollection()
        def __init__(self):         
            self.classDict = {}
            self.relationshipDict = {}

        # self.getClass(name).addAttribute(attributeName)
        # self.addAttribute(className, attributeName) -> className.addAttribute(attributeName)

        ## Cast the user's name input to a string, creates
        ## a new dictionary entry for that name and assigns
        ## it the value of the class Object
        ##
        ## Ex:   collection1.addClass("ClassX")
        def addClass(self, name):
            

        ## Cast the user's name input to a string, search 
        ## for the dictionary entry with that name, and remove
        ## that entry. Remove existing relationsips that contain 
        ## that class name.
        ##
        ## Ex:   collection1.deleteClass("ClassX")
        def deleteClass(self, name):
            
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



        def addRelationship(self, firstClassName, secondClassName):
        
        def deleteRelationship(self, firstClassName, secondClassName):
            

           
        def addAttribute(self, className, attributeName):
        
        def deleteAttribute(self, className, attributeName):
            
        def renameAttribute(self, className, oldAttributeName, newAttributeName):



