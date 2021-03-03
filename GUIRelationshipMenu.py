# Contains classes used to create menus related to relationships

from PyQt5.QtWidgets import QWidget, QDialog, QLabel, QLineEdit, QComboBox, QPushButton

class RelationshipMenu(QDialog):
        
    def __init__(self, parent = None):
        super(RelationshipMenu, self).__init__(parent)

    def addRelationship(self):
        self.setWindowTitle('Add Relationship')
        # w, h
        self.setFixedSize(350, 405)
        self.setStyleSheet(open('MenuStyleSheet.css').read()) 
        self.setModal(True)

        lblSrcClass = QLabel("Source Class", parent = self)
        lblSrcClass.move(50, 50)
        txtSrcClass = QLineEdit(self)
        txtSrcClass.move(50, 85)
        txtSrcClass.resize(250, 30)

        lblDestClass = QLabel("Destination Class", parent = self)
        lblDestClass.move(50, 135)
        txtDestClass = QLineEdit(self)
        txtDestClass.move(50, 170)
        txtDestClass.resize(250, 30)

        lblRelationshipType = QLabel("Relationship Type", parent = self)
        lblRelationshipType.move(50, 220)
        cbxRelationshipType = QComboBox(self)
        cbxRelationshipType.move(50, 255)
        cbxRelationshipType.addItems(["Aggregation", "Composition", "Inheritance", "Realization"])

        btnSubmit = QPushButton(self)
        btnSubmit.setText("Submit")
        btnSubmit.move(50, 305) 
        btnSubmit.resize(250, 50)

        # This needs to be an anonymous function for the signal to work
        btnSubmit.clicked.connect(lambda: self.addRelationshipData(txtSrcClass.text(), txtDestClass.text(), cbxRelationshipType.currentText()))

        self.exec_()

    # TODO: right now this takes the information entered into the menu and prints the data.
    # This information needs to be sent to the controller instead of being printed
    def addRelationshipData(self, firstClassName, secondClassName, typ):
        self.close()
        print(firstClassName)
        print(secondClassName)
        print(typ)


    def deleteRelationship(self):
        self.setWindowTitle('Delete Relationship')
        # w, h
        self.setFixedSize(350, 335)
        self.setStyleSheet(open('MenuStyleSheet.css').read()) 
        self.setModal(True)

        lblSrcClass = QLabel("Source Class", parent = self)
        lblSrcClass.move(50, 50)
        txtSrcClass = QLineEdit(self)
        txtSrcClass.move(50, 85)
        txtSrcClass.resize(250, 30)

        lblDestClass = QLabel("Destination Class", parent = self)
        lblDestClass.move(50, 135)
        txtDestClass = QLineEdit(self)
        txtDestClass.move(50, 170)
        txtDestClass.resize(250, 30)

        btnSubmit = QPushButton(self)
        btnSubmit.setText("Submit")
        btnSubmit.move(50, 235) 
        btnSubmit.resize(250, 50)

        # This needs to be an anonymous function for the signal to work
        btnSubmit.clicked.connect(lambda: self.delRelationshipData(txtSrcClass.text(), txtDestClass.text()))

        self.exec_()

    # TODO: right now this takes the information entered into the menu and prints the data.
    # This information needs to be sent to the controller instead of being printed
    def delRelationshipData(self, firstClassName, secondClassName):
        self.close()
        print(firstClassName)
        print(secondClassName)


    def renameRelationship(self):
        self.setWindowTitle('Change Relationship')
        # w, h
        self.setFixedSize(350, 405)
        self.setStyleSheet(open('MenuStyleSheet.css').read()) 
        self.setModal(True)

        lblSrcClass = QLabel("Source Class", parent = self)
        lblSrcClass.move(50, 50)
        txtSrcClass = QLineEdit(self)
        txtSrcClass.move(50, 85)
        txtSrcClass.resize(250, 30)

        lblDestClass = QLabel("Destination Class", parent = self)
        lblDestClass.move(50, 135)
        txtDestClass = QLineEdit(self)
        txtDestClass.move(50, 170)
        txtDestClass.resize(250, 30)

        lblRelationshipType = QLabel("Relationship Type", parent = self)
        lblRelationshipType.move(50, 220)
        cbxRelationshipType = QComboBox(self)
        cbxRelationshipType.move(50, 255)
        cbxRelationshipType.addItems(["Aggregation", "Composition", "Inheritance", "Realization"])

        btnSubmit = QPushButton(self)
        btnSubmit.setText("Submit")
        btnSubmit.move(50, 305) 
        btnSubmit.resize(250, 50)

        # This needs to be an anonymous function for the signal to work
        btnSubmit.clicked.connect(lambda: self.renRelationshipData(txtSrcClass.text(), txtDestClass.text(), cbxRelationshipType.currentText()))

        self.exec_()

    # TODO: right now this takes the information entered into the menu and prints the data.
    # This information needs to be sent to the controller instead of being printed
    def renRelationshipData(self, firstClassName, secondClassName, typ):
        self.close()
        print(firstClassName)
        print(secondClassName)
        print(typ)

