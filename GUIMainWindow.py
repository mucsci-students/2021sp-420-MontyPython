# Handles exit status
import sys

# Import Qapplication and required widgets
from PyQt5.QtWidgets import QApplication, QWidget, QMenuBar, QMenu, QLabel, QMainWindow, QAction, QPushButton, QDesktopWidget
from PyQt5.QtGui import QPainter, QPen
from GUIClassWidget import ClassWidget

class MainWindow(QWidget):
        
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        
        self.menuObjects = {}

        self.drawWindow()
        self.centerWindow()
        self.drawMenuBar()

    def drawWindow(self):
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

        # Submenu: Edit Elements -- Class
        self.menuObjects["Add Class"] = menuClass.addAction("Add Class")
        self.menuObjects["Delete Class"] = menuClass.addAction("Delete Class")
        self.menuObjects["Rename Class"] = menuClass.addAction("Rename Class")

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
        self.menuObjects["Delete Parameter"] = menuMethod.addAction("Delete Parameter")
        self.menuObjects["Change Parameter"] = menuMethod.addAction("Change Parameter")

        # Submenu: Edit Elements -- Relationship
        self.menuObjects["Add Relationship"] = menuRelationship.addAction("Add Relationship")
        self.menuObjects["Delete Relationship"] = menuRelationship.addAction("Delete Relationship")
        self.menuObjects["Change Relationship"] = menuRelationship.addAction("Change Relationship")


    # ----------- Anything below this line can be ignored until sprint 3 ----------- #
    # TODO
    def createRClickMenu(self):
        pass
        # Causes widgets that have actions to show them in a context menu
        # https://www.youtube.com/watch?v=75yvkmXE0wM
        #classLabel.setContextMenuPolicy(Qt.ActionsContextMenu)
        #classLabel.addAction("Delete Relationship")

    # TODO: QMessageBox for popups like "Are you sure you'd like to save?"
    # TODO - Make sure window size is saved when user saves the state of the program