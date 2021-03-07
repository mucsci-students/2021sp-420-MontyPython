import sys
from ClassCollection import ClassCollection
from PyQt5.QtWidgets import QLabel
import GUIController, GUIClassMenu, GUIRelationshipMenu, GUIFieldMenu, GUIParameterMenu, GUIMethodMenu, GUIBrowseFiles
from GUIClassWidget import ClassWidget

# A default collection
collection = ClassCollection()

class GUIController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.classWidgetDictionary = {}
        self.classWidgetCount = 0
        # TODO: For sprint 3, the biggest flaw in this is it doesn't scale for the class widget size. Fix this and
        # create something that dynamically scales
        self.coordinateList = [[50, 100], [50, 400], [400, 100], [400, 400], [800, 100], [800, 800]]

        # -------------- Sprint 3 -------------- #
        #self.setSignal("Open", self.openMenu)
        #self.setSignal("Save", self.saveMenu)
        # -------------------------------------- #
        self.setSignal("Help", self.helpMenu)
        self.setSignal("Exit", self.exit)

        self.setSignal("Add Class", self.addClassMenu)
        self.setSignal("Delete Class", self.delClassMenu)
        self.setSignal("Rename Class", self.renClassMenu)

        self.setSignal("Add Field", self.addFieldMenu)
        self.setSignal("Delete Field", self.delFieldMenu)
        self.setSignal("Rename Field", self.renFieldMenu)

        self.setSignal("Add Method", self.addMethodMenu)
        self.setSignal("Delete Method", self.delMethodMenu)
        self.setSignal("Rename Method", self.renMethodMenu)

        self.setSignal("Add Parameter", self.addParamMenu)
        self.setSignal("Delete Parameter", self.delParamMenu)
        self.setSignal("Change Parameter", self.chgParamMenu)

        self.setSignal("Add Relationship", self.addRelationshipMenu)
        self.setSignal("Delete Relationship", self.delRelationshipMenu)
        self.setSignal("Change Relationship", self.renRelationshipMenu)

        # TODO: Major bug: class widgets make top menu inaccessible
        # Temporary fix: Every time new widget is added, menu bar has to be redrawn over it
        # Note: That works, but breaks all buttons
        classWidget = ClassWidget(view, self.coordinateList[0][0], self.coordinateList[0][1], "Book", "title: String\nauthors : String[]", "getTitle(): String[]\ngetAuthors() : String[]\naddAuthor(name)")
        classWidget = ClassWidget(view, self.coordinateList[1][0], self.coordinateList[1][1], "Book", "title: String\nauthors : String[]", "getTitle(): String[]\ngetAuthors() : String[]\naddAuthor(name)")
        classWidget = ClassWidget(view, self.coordinateList[2][0], self.coordinateList[2][1], "Book", "title: String\nauthors : String[]", "getTitle(): String[]\ngetAuthors() : String[]\naddAuthor(name)")
        classWidget = ClassWidget(view, self.coordinateList[3][0], self.coordinateList[3][1], "Book", "title: String\nauthors : String[]", "getTitle(): String[]\ngetAuthors() : String[]\naddAuthor(name)")
        classWidget = ClassWidget(view, self.coordinateList[4][0], self.coordinateList[4][1], "Book", "title: String\nauthors : String[]", "getTitle(): String[]\ngetAuthors() : String[]\naddAuthor(name)")
        
        #view.drawLines(400, 100, 200, 100)
        #print(classWidget.getCoordinates())
        #classWidget.setCoordinates(20, 20)
        #print(classWidget.getCoordinates())
        #classWidget.setName("Testing")
        #classWidget.delete()


    def setSignal(self, name, function):
        self.view.menuObjects[name].triggered.connect(function)

    def open(self):
        pass

    def save(self):
        pass

    def help(self):
        pass

    def exit(self):
        sys.exit()

    def addClass(self, name):
        # Add new class widget to the view
        pass

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

    # -------------- Sprint 3 -------------- #
    #def openMenu(self, checked):
        #self.oMenu = GUIBrowseFiles.BrowseFiles().openFile(self)

    #def saveMenu(self, checked):
        #self.sMenu = GUIBrowseFiles.BrowseFiles().saveFile(self)
    # -------------------------------------- #

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

    def chgParamMenu(self, checked):
        self.renPMenu = GUIParameterMenu.ParameterMenu().changeParameter(self)

    def delRelationshipMenu(self, checked):
        self.delRMenu = GUIRelationshipMenu.RelationshipMenu().deleteRelationship(self)

    def renRelationshipMenu(self, checked):
        self.renRMenu = GUIRelationshipMenu.RelationshipMenu().renameRelationship(self)
    
    def helpMenu(self, checked):
        print('help was clicked yay')


# Create a method to pull info about classes from a class collection instance. Maybe that should be made here?
# This may end up being similar to interface.py and REPL.py
