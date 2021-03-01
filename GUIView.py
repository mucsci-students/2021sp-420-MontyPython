# Handles exit status
import sys
import GUIController

# Import Qapplication and required widgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
# For the menu bar at the top
from PyQt5.QtWidgets import QMenuBar
from PyQt5.QtWidgets import QMenu
# For individual Classes
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMainWindow

from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QPushButton

# TODO: Figure out circular problem with the guicontroller and gui

# TODO: Figure out the difference between QWidget and QMainWindow
class MainWindow(QWidget):
        
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        
        self.drawWindow()
        self.drawMenuBar()
        self.drawClass()
        

    def drawWindow(self):
        # The window is created in GuiController.py
        self.setWindowTitle('UML Editor')

        # Window size: x and y coords on screen, width and height of window
        # TODO: The coords will be problematic based on screen size. Fix this so it centers at any screen size (desktop()/screenGeometry()?)
        self.setGeometry(500, 500, 500, 500)

        # Style sheet can be used on all parts of GUI
        self.setStyleSheet(open('GuiStyleSheet.css').read()) 
        
    def drawMenuBar(self):
        # Create bar
        #self.bar = QMenuBar()
        # TODO - Are memory leaks possible?
        bar = QMenuBar(self)

        # Add menus to bar
        menuFile = bar.addMenu("File")
        menuEditElements = bar.addMenu("Edit Elements")

        # Add submenus and connect signals to
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
        menuAddClass = menuEditElements.addAction("Add Class")
        menuAddClass.triggered.connect(self.drawClass)
        menuDeleteClass = menuEditElements.addAction("Delete Class")
        menuDeleteClass.triggered.connect(test1)
        menuRenameClass = menuEditElements.addAction("Rename Class")
        menuRenameClass.triggered.connect(test1)
        menuEditElements.addSeparator()

        # Submenu: Edit Elements -- Attribute
        menuAddAttribute = menuEditElements.addAction("Add Attribute")
        menuAddAttribute.triggered.connect(test1)
        menuDeleteAttribute = menuEditElements.addAction("Delete Attribute")
        menuDeleteAttribute.triggered.connect(test1)
        menuRenameAttribute = menuEditElements.addAction("Rename Attribute")
        menuRenameAttribute.triggered.connect(test1)
        menuEditElements.addSeparator()

        # Submenu: Edit Elements -- Relationship
        menuAddRelationship = menuEditElements.addAction("Add Relationship")
        menuAddRelationship.triggered.connect(test1)
        menuDeleteRelationship = menuEditElements.addAction("Delete Relationship")
        menuDeleteRelationship.triggered.connect(test1)

    # This will be called when a class is added or a class is being loaded.
    # It'll pull info from GuiController.py
    def drawClass(self):
        # x and y coords for labels are based on the top left corner of the label
        x = 200
        y = 200

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
        fieldLbl.setGeometry(x, y, width, fieldHeight)
        # Adding/subtracting 2 makes the lines overlap and makes it appear as though it's one object
        nameLbl.setGeometry(fieldLbl.x(), (fieldLbl.y() - nameHeight + 2), width, nameHeight)
        methodLbl.setGeometry(fieldLbl.x(), (fieldLbl.y() + fieldHeight - 2), width, methodHeight)

    # TODO
    def createRClickMenu(self):
        print("test")
        # Causes widgets that have actions to show them in a context menu
        # https://www.youtube.com/watch?v=75yvkmXE0wM
        #classLabel.setContextMenuPolicy(Qt.ActionsContextMenu)
        #classLabel.addAction("Delete Relationship")

def test1():
    print("test")

    
    # Menu when label is right clicked
        # Use drop down or multiple selection within the menu
    # Idea: Have fixed spots on the editor that classes can be dragged and snapped into

    # Lines between labels

    # Popup dialog that asks for info when you add a class/attribute/etc

     # TODO - Delete this when done testing
        #btn1 = QPushButton(self)
        #btn1.move(80, 80)
        #btn1.clicked.connect(test1)