from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtCore import Qt

class ClassWidget(QWidget):
        
    def __init__(self, parentWindow, x, y, name, field, method):
        super(ClassWidget, self).__init__(parent = parentWindow)

        # This is for sprint 3
        self.clicked = False

        self.x = x
        self.y = y
        self.name = name
        self.field = field
        self.method = method
        
        # Create label instances contained within this widget
        self.nameLbl = QLabel(self.name, parent = self)
        self.fieldLbl = QLabel(self.field, parent = self)
        self.methodLbl = QLabel(self.method, parent = self)

        self.drawClass()
    
    # Sets new coordinates for the widget and updates the widget location
    # Note: x and y coords for labels are based on the top left corner of the label
    def setCoordinates(self, newX, newY):
        self.x = newX
        self.y = newY
        self.drawClass()

    # Returns the current coordinates of the widget
    def getCoordinates(self):
        return [self.x, self.y]

    # Updates name label text
    def setName(self, newName):
        self.name = newName
        self.nameLbl.setText(newName)

    # Updates field label text
    def setField(self, newField):
        self.field = newField
        self.fieldLbl.setText(newField)
    
    # Updates method label text
    def setMethod(self, newMethod):
        self.method = newMethod
        self.methodLbl.setText(newMethod)

    # Deletes the instance of Class Widget
    def delete(self):
        self.close()

    def drawClass(self):

        # Did this so names would be easier to read (self won't be everywhere)
        x = self.x
        y = self.y
        nameLbl = self.nameLbl
        methodLbl = self.methodLbl
        fieldLbl = self.fieldLbl

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

        # Base location of all labels around nameLbl
        nameLbl.setGeometry(x, y, width, nameHeight)
        fieldLbl.setGeometry(x, (y + nameHeight - 2), width, fieldHeight)
        # Adding/subtracting the extra number makes the lines overlap, so it looks like all three textboxes are one object
        methodLbl.setGeometry(x, (y + fieldHeight + nameHeight - 4), width, methodHeight)


    # --------- Anything below this can be ignored until sprint 3 --------- #
    def mousePressEvent(self, event):
        # Location of the mouse when the button is first clicked
        self.startLoc = event.pos()
        self.clicked = True

    def mouseMoveEvent(self, event):
        # This will continue until mouseReleaseEvent is triggered, because that's how it gets set to false
        if self.clicked and event.buttons() == Qt.LeftButton:

            # Current location of the mouse
            self.endLoc = event.pos()
            # The change in distance
            self.locChange = self.mapToGlobal(self.endLoc - self.startLoc)
            self.move(self.locChange)
            # Continuously update until the mouseReleaseEvent is triggered
            self.endLoc = self.startLoc

    def mouseReleaseEvent(self, event):
        self.clicked = False
