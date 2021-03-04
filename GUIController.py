import sys
from ClassCollection import ClassCollection
from PyQt5.QtWidgets import QLabel
import GUIController, GUIClassMenu, GUIRelationshipMenu, GUIFieldMenu, GUIParameterMenu, GUIMethodMenu, GUIBrowseFiles

# A default collection
collection = ClassCollection()

class GUIController:
    def __init__(self, model):
        self.model = model
    
    def open(self):
        pass

    def save(self):
        pass

    def help(self):
        pass

    def exit(self):
        sys.exit()

    def addClass(self, name):
        print(f'{name} IN CONTROLLER')
        # Take the info from the addClass menu, store in the classcollection and find a way to display it on the main window

    def deleteClass(self, name):
        pass
        # Take the name of the class from the menu, update the classcollection, and delete the class from the main window

    def renameClass(self, oldName, newName):
        pass

    def addRelationship(self, firstClassName, secondClassName, typ):
        pass

    def deleteRelationship(self, firstClassName, secondClassName):
        pass

    def renameRelationship(self, firstClassName, secondClassName, typ):
        pass

    def addMethod(self, className, methodName, returnType, parameters):
        pass

    def deleteMethod(self, className, methodName):
        pass

    def renameMethod(self, className, methodName, newName):
        pass

    def addParameter(self, className, methodName, typ, name):
        pass

    def removeParameter(self, className, methodName, name):
        pass

    def changeParameter(self, className, methodName, name, newType, newName):
        pass

    def addField(self, className, name, dataType):
        pass

    def deleteField(self, className, name):
        pass

    def renameField(self, className, oldName, newName):
        pass

    # Creates instance of popup windows
    def addClassMenu(self, checked):
        self.cMenu = GUIClassMenu.ClassMenu().addClass(self)
 
    def addRelationshipMenu(self, checked):
        self.rMenu = GUIRelationshipMenu.RelationshipMenu().addRelationship(self)

    def addFieldMenu(self, checked):
        self.fMenu = GUIFieldMenu.FieldMenu().addField(self)
    
    def addMethodMenu(self, checked):
        self.mMenu = GUIMethodMenu.MethodMenu().addMethod(self)

    def addParamMenu(self, checked):
        self.pMenu = GUIParameterMenu.ParameterMenu().addParameter(self)

    def openMenu(self, checked):
        self.oMenu = GUIBrowseFiles.BrowseFiles().openFile(self)

    def saveMenu(self, checked):
        self.sMenu = GUIBrowseFiles.BrowseFiles().saveFile(self)

    def delClassMenu(self, checked):
        self.delCMenu = GUIClassMenu.ClassMenu().deleteClass(self)

    def renClassMenu(self, checked):
        self.renCMenu = GUIClassMenu.ClassMenu().renameClass(self)

    def delFieldMenu(self, checked):
        self.delFMenu = GUIFieldMenu.FieldMenu().deleteField(self)

    def renFieldMenu(self, checked):
        self.renFMenu = GUIFieldMenu.FieldMenu().renameField(self)

    def delMethodMenu(self, checked):
        self.delMethodMenu = GUIMethodMenu.MethodMenu().deleteMethod(self)

    def renMethodMenu(self, checked):
        self.renMethodMenu = GUIMethodMenu.MethodMenu().renameMethod(self)

    def delParamMenu(self, checked):
        self.delPMenu = GUIParameterMenu.ParameterMenu().deleteParameter(self)

    def chgParameterMenu(self, checked):
        self.renPMenu = GUIParameterMenu.ParameterMenu().changeParameter(self)

    def delRelationshipMenu(self, checked):
        self.delRMenu = GUIRelationshipMenu.RelationshipMenu().deleteRelationship(self)

    def renRelationshipMenu(self, checked):
        self.renRMenu = GUIRelationshipMenu.RelationshipMenu().renameRelationship(self)


# Create a method to pull info about classes from a class collection instance. Maybe that should be made here?
# This may end up being similar to interface.py and REPL.py
