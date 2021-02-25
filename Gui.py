# Handles exit status
import sys

# Import Qapplication and required widgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMenuBar

# QApplication instance, pass in sys.argv because it deals with common command line args
qApp = QApplication(sys.argv)

# ------------------ View ------------------ #

# Create application GUI instance
window = QWidget()
window.setWindowTitle('UML Editor')

# Window size: x and y coords on screen, width and height of window
# TODO: The coords will be problematic based on screen size. Fix this so it centers at any screen size
window.setGeometry(500, 500, 500, 500)


window.setStyleSheet(open('GuiStyleSheet.css').read()) 

bar = QMenuBar(window)

menuFile = bar.addMenu("File")
menuEditElements = bar.addMenu("Edit Elements")

menuFile.addAction("Open")
menuFile.addAction("Save")
menuFile.addSeparator()
menuFile.addAction("Help")
menuFile.addSeparator()
menuFile.addAction("Exit")

# ``````````````````````````````

addClass = QAction("Add Class", window)
menuEditElements.addAction(addClass)

def clicked(window, text):
    window.


# ``````````````````````````````

menuEditElements.addAction("Delete Class")
menuEditElements.addAction("Rename Class")
menuEditElements.addSeparator()

menuEditElements.addAction("Add Attribute")
menuEditElements.addAction("Delete Attribute")
menuEditElements.addAction("Rename Attribute")
menuEditElements.addSeparator()

menuEditElements.addAction("Add Relationship")
menuEditElements.addAction("Delete Relationship")

# Top Menu Bar

# Label to show class?
# Box around the label?
# Menu when label is right clicked
# Idea: Have fixed spots on the editor that classes can be dragged and snapped into

# Lines between labels

# Popup dialog that asks for info when you add a class/attribute/etc