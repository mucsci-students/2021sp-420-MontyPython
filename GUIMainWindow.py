# Handles exit status
import sys
import GUIController, GUIClassMenu, GUIRelationshipMenu, GUIFieldMenu, GUIParameterMenu, GUIMethodMenu

# Import Qapplication and required widgets
from PyQt5.QtWidgets import QApplication, QWidget, QMenuBar, QMenu, QLabel, QMainWindow, QAction, QPushButton, QDesktopWidget
from PyQt5.QtGui import QPainter, QPen

# TODO: Figure out the difference between QWidget and QMainWindow
class MainWindow(QWidget):
        
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        
        self.drawWindow()
        self.centerWindow()
        self.drawMenuBar()

        # TODO - Delete this when done testing
        self.drawClass(100, 200)
        self.drawClass(400, 200)

    def drawWindow(self):
        # The window is created in GuiController.py
        self.setWindowTitle('UML Editor')

        # Width, height
        self.resize(800, 800)

        # Style sheet can be used on all parts of GUI
        self.setStyleSheet(open('GuiStyleSheet.css').read()) 

    def centerWindow(self):
        # Get widget geometry
        widgetGeo = self.frameGeometry()
        # Find the center of the desktop 
        centerScreen = QDesktopWidget().availableGeometry().center()
        # Move the widget center to the center of the screen
        widgetGeo.moveCenter(centerScreen)
        self.move(widgetGeo.topLeft())
        
    def drawMenuBar(self):
        # Create bar
        #self.bar = QMenuBar()
        # TODO - Are memory leaks possible?
        # TODO - Stretch the menu bar across the top of the GUI
        bar = QMenuBar(self)

        # Add menus to bar
        menuFile = bar.addMenu("File")
        menuClass = bar.addMenu("Classes")
        menuField = bar.addMenu("Fields")
        menuMethod = bar.addMenu("Methods")

        menuRelationship = bar.addMenu("Relationships")

        # Add submenus and connect signals to them
        # Submenu: File  
        menuOpen = menuFile.addAction("Open")
        menuOpen.triggered.connect(test1)
        menuSave = menuFile.addAction("Save")
        menuSave.triggered.connect(test1)
        menuFile.addSeparator()
        menuHelp = menuFile.addAction("Help")
        menuHelp.triggered.connect(test1)
        menuFile.addSeparator()
        menuExit = menuFile.addAction("Exit")
        menuExit.triggered.connect(GUIController.exit)

        # Submenu: Edit Elements -- Class
        menuAddClass = menuClass.addAction("Add Class")
        menuAddClass.triggered.connect(self.openClassMenu)
        menuDeleteClass = menuClass.addAction("Delete Class")
        menuDeleteClass.triggered.connect(test1)
        menuRenameClass = menuClass.addAction("Rename Class")
        menuRenameClass.triggered.connect(test1)

        # Submenu: Edit Elements -- Field
        menuAddField = menuField.addAction("Add Field")
        menuAddField.triggered.connect(self.openFieldMenu)
        menuDeleteField = menuField.addAction("Delete Field")
        menuDeleteField.triggered.connect(test1)
        menuRenameField = menuField.addAction("Rename Field")
        menuRenameField.triggered.connect(test1)

        # Submenu: Edit Elements -- Method
        menuAddMethod = menuMethod.addAction("Add Method")
        menuAddMethod.triggered.connect(self.openMethodMenu)
        menuDeleteMethod = menuMethod.addAction("Delete Method")
        menuDeleteMethod.triggered.connect(test1)
        menuRenameMethod = menuMethod.addAction("Rename Method")
        menuRenameMethod.triggered.connect(test1)
        menuMethod.addSeparator()

        # Submenu: Edit Elements -- Parameter
        menuAddParameter = menuMethod.addAction("Add Parameter")
        menuAddParameter.triggered.connect(self.openParamMenu)
        menuDeleteParameter = menuMethod.addAction("Delete Parameter")
        menuDeleteParameter.triggered.connect(test1)
        menuRenameParameter = menuMethod.addAction("Rename Parameter")
        menuRenameParameter.triggered.connect(test1)

        # Submenu: Edit Elements -- Relationship
        menuAddRelationship = menuRelationship.addAction("Add Relationship")
        menuAddRelationship.triggered.connect(self.openRelationshipMenu)
        menuDeleteRelationship = menuRelationship.addAction("Delete Relationship")
        menuDeleteRelationship.triggered.connect(test1)

    # This will be called when a class is added or a class is being loaded.
    # It'll pull info from GuiController.py
    def drawClass(self, x, y):
        # x and y coords for labels are based on the top left corner of the label

        # TODO: What if field and method labels are empty?
        # TODO: Add parameters nameLbl, fieldLbl, methodLbl

        nameLbl = QLabel("Book", parent = self)
        fieldLbl = QLabel("title: String\nauthors : String[]", parent = self)
        methodLbl = QLabel("getTitle(): String[]\ngetAuthors() : String[]\naddAuthor(name)", parent = self)

        # Start by automatically setting the size of each label based on the contents
        methodLbl.adjustSize()
        fieldLbl.adjustSize()
        nameLbl.adjustSize()

        # Set width of all three based on whichever is the largest
        if methodLbl.width() > fieldLbl.width() and methodLbl.width() > nameLbl.width():
            width = methodLbl.width()
        elif fieldLbl.width() > methodLbl.width() and fieldLbl.width() > nameLbl.width():
            width = fieldLbl.width()
        elif nameLbl.width() > fieldLbl.width() and nameLbl.width() > methodLbl.width():
            width = nameLbl.width()

        # Get the auto heights
        fieldHeight = fieldLbl.height()
        nameHeight = nameLbl.height()
        methodHeight = methodLbl.height()

        # Base everything around fieldLbl(It's in the middle of name and method)
        # TODO: Maybe change this to nameLbl. What if there are no field/methods? How will it display?
        fieldLbl.setGeometry(x, y, width, fieldHeight)
        # Adding/subtracting 2 makes the lines overlap and makes it appear as though it's one object
        nameLbl.setGeometry(fieldLbl.x(), (fieldLbl.y() - nameHeight + 2), width, nameHeight)
        methodLbl.setGeometry(fieldLbl.x(), (fieldLbl.y() + fieldHeight - 2), width, methodHeight)

        # TODO: Track mouse movement to place class label w/ a click, move w/ another click

    def openClassMenu(self, checked):
        self.cMenu = GUIClassMenu.ClassMenu().addClass()
 
    def openRelationshipMenu(self, checked):
        self.rMenu = GUIRelationshipMenu.RelationshipMenu().addRelationship()

    def openFieldMenu(self, checked):
        self.fMenu = GUIFieldMenu.FieldMenu().addField()
    
    def openMethodMenu(self, checked):
        self.mMenu = GUIMethodMenu.MethodMenu().addMethod()

    def openParamMenu(self, checked):
        self.pMenu = GUIParameterMenu.ParameterMenu().addParameter()

    # TODO
    def createRClickMenu(self):
        print("test")
        # Causes widgets that have actions to show them in a context menu
        # https://www.youtube.com/watch?v=75yvkmXE0wM
        #classLabel.setContextMenuPolicy(Qt.ActionsContextMenu)
        #classLabel.addAction("Delete Relationship")

# TODO: Delete this when done testing
def test1():
    print("test")

    # TODO: QMessageBox for popups like "Are you sure you'd like to save?"
    # Use QDialog for the menu?

    # TODO: Relationship lines between labels

     # TODO - Delete this when done testing
        #btn1 = QPushButton(self)
        #btn1.move(80, 80)
        #btn1.clicked.connect(test1)

    # TODO - Make sure window size is saved when user saves the state of the program