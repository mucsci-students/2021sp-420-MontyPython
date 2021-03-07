# Handles exit status
import sys

# Import Qapplication and required widgets
from PyQt5.QtWidgets import QApplication, QWidget, QMenuBar, QMenu, QLabel, QMainWindow, QAction, QPushButton, QDesktopWidget
from PyQt5.QtGui import QPainter, QPen, QBrush
from PyQt5.QtCore import Qt


# TODO: Figure out the difference between QWidget and QMainWindow
class MainWindow(QWidget):
        
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        
        self.menuObjects = {}
        self.RelationshipCoordiantes = {}    #[(joe, secondClassName)] = [x1, y1, x2, y2]
        #self.addRelationshipLine("firstClassName", "secondClassName", 200, 100, 400, 200)
        self.drawWindow()
        self.centerWindow()
        self.drawMenuBar()

        #self.drawLines()

        # TODO - Delete this when done testing

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
        bar = QMenuBar(self)

        # w, h
        # TODO: Fix this so it goes across when window is resized
        bar.resize(800, 30)

        # Add menus to bar
        menuFile = bar.addMenu("File")
        menuClass = bar.addMenu("Classes")
        menuField = bar.addMenu("Fields")
        menuMethod = bar.addMenu("Methods")
        menuRelationship = bar.addMenu("Relationships")
        
        # Add submenus and connect signals to them
        # Submenu: File  
        self.menuObjects["Open"] = menuFile.addAction("Open")
        self.menuObjects["Save"] = menuFile.addAction("Save")
        menuFile.addSeparator()
        self.menuObjects["Help"] = menuFile.addAction("Help")
        menuFile.addSeparator()
        self.menuObjects["Exit"] = menuFile.addAction("Exit")
        # menuExit.triggered.connect(self.controller.exit)

        # Submenu: Edit Elements -- Class
        self.menuObjects["Add Class"] = menuClass.addAction("Add Class")
        # menuAddClass.triggered.connect(self.controller.addClassMenu)
        self.menuObjects["Delete Class"] = menuClass.addAction("Delete Class")
        # menuDeleteClass.triggered.connect(self.controller.delClassMenu)
        self.menuObjects["Rename Class"] = menuClass.addAction("Rename Class")
        # menuRenameClass.triggered.connect(self.controller.renClassMenu)

        # Submenu: Edit Elements -- Field
        self.menuObjects["Add Field"] = menuField.addAction("Add Field")
        self.menuObjects["Delete Field"] = menuField.addAction("Delete Field")
        self.menuObjects["Rename Field"] = menuField.addAction("Rename Field")

        # Submenu: Edit Elements -- Method
        self.menuObjects["Add Method"] = menuMethod.addAction("Add Method")
        self.menuObjects["Delete Method"] = menuMethod.addAction("Delete Method")
        self.menuObjects["Rename Method"] = menuMethod.addAction("Rename Method")
        menuMethod.addSeparator()

        # Submenu: Edit Elements -- Parameter
        self.menuObjects["Add Parameter"] = menuMethod.addAction("Add Parameter")
        # menuAddParameter.triggered.connect(self.controller.addParamMenu)
        self.menuObjects["Delete Parameter"] = menuMethod.addAction("Delete Parameter")
        # menuDeleteParameter.triggered.connect(self.controller.delParamMenu)
        self.menuObjects["Change Parameter"] = menuMethod.addAction("Change Parameter")
        # menuRenameParameter.triggered.connect(self.controller.chgParameterMenu)

        # Submenu: Edit Elements -- Relationship
        self.menuObjects["Add Relationship"] = menuRelationship.addAction("Add Relationship")
        self.menuObjects["Delete Relationship"] = menuRelationship.addAction("Delete Relationship")
        # menuDeleteRelationship.triggered.connect(self.controller.delRelationshipMenu)
        self.menuObjects["Change Relationship"] = menuRelationship.addAction("Change Relationship")
        # menuRenameRelationship.triggered.connect(self.controller.renRelationshipMenu)

    # This will be called when a class is added or a class is being loaded.
    # It'll pull info from GuiController.py
    # TODO: Add parameters nameLbl, fieldLbl, methodLbl
    def drawClass(self, x, y):
        # x and y coords for labels are based on the top left corner of the label

        # TODO: What if field and method labels are empty?

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

    def paintEvent(self, event):
        paint = QPainter()
        paint.begin(self)
        paint.fillRect(0, 0, 1000, 800, QBrush(Qt.white))
        self.drawLines(paint)
        paint.end()


    def drawLines(self, paint):
        penSolid = QPen(Qt.black, 2)
        paint.setPen(penSolid)
        paint.drawLine(400, 100, 200, 100)
        for key, x in self.RelationshipCoordiantes.items():
            paint.drawLine(x[0], x[1], x[2], x[3])


    def addRelationshipLine(self, firstClassName, secondClassName, x1, y1, x2, y2):
        self.RelationshipCoordiantes[(firstClassName, secondClassName)] = [x1, y1, x2, y2]

    def deleteRelationshipLine(self, firstClassName, secondClassName):
        del self.RelationshipCoordiantes[(firstClassName, secondClassName)]




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

    # TODO - Make sure window size is saved when user saves the state of the program