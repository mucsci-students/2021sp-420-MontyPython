from PyQt5.QtWidgets import QWidget, QLabel

class ClassWidget(QWidget):
        
    def __init__(self, parentWindow, x, y, name, field, method):
        super(ClassWidget, self).__init__(parent = parentWindow)

        self.clicked = False

        self.x = x
        self.y = y
        self.name = name
        self.field = field
        self.method = method

        drawClass(self)
        # x and y coords for labels are based on the top left corner of the label

        # TODO: What if field and method labels are empty?

    def drawClass(self)

        nameLbl = QLabel(self.name, parent = self)
        fieldLbl = QLabel(self.field, parent = self)
        methodLbl = QLabel(self.method, parent = self)

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
        fieldLbl.setGeometry(self.x, self.y, width, fieldHeight)
        # Adding/subtracting 2 makes the lines overlap and makes it appear as though it's one object
        nameLbl.setGeometry(fieldLbl.x(), (fieldLbl.y() - nameHeight + 2), width, nameHeight)
        methodLbl.setGeometry(fieldLbl.x(), (fieldLbl.y() + fieldHeight - 2), width, methodHeight)

        # TODO: Track mouse movement to place class label w/ a click, move w/ another click

    def mousePressEvent(self, QMouseEvent):
        # Location of the mouse when the button is first clicked
        self.startLoc = QMouseEvent.pos()
        self.clicked = True

    def mouseMoveEvent(self, QMouseEvent):
        # This will continue until mouseReleaseEvent is triggered, because that's how it gets set to false
        if self.clicked and QMouseEvent.type() == Qt.LeftButton():
            # Current location of the mouse
            self.endLoc = QMouseEvent.pos()
            # The change in distance
            self.locChange = self.mapToGlobal(self.end - self.start)
            self.move(self.locChange)
            # Continuously update until the mouseReleaseEvent is triggered
            self.endLoc = self.startLoc

    def mouseReleaseEvent(self, QMouseEvent):
        self.clicked = False
