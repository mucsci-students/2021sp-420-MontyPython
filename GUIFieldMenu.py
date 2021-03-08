# This file contains all menus related to entering/deleting field data

from PyQt5.QtWidgets import QWidget, QDialog, QLabel, QLineEdit, QPushButton

class FieldMenu(QDialog):
        
    def __init__(self, parent = None):
        super(FieldMenu, self).__init__(parent)

    def addField(self, controller):
        self.setWindowTitle('Add Field')
        # w, h
        self.setFixedSize(350, 405)
        self.setStyleSheet(open('MenuStyleSheet.css').read()) 
        self.setModal(True)

        lblClassName = QLabel("Class Name", parent = self)
        lblClassName.move(50, 50)
        txtClassName = QLineEdit(self)
        txtClassName.move(50, 85)
        txtClassName.resize(250, 30)

        lblFieldName = QLabel("Field Name", parent = self)
        lblFieldName.move(50, 135)
        txtFieldName = QLineEdit(self)
        txtFieldName.move(50, 170)
        txtFieldName.resize(250, 30)

        lblType = QLabel("Field Data Type", parent = self)
        lblType.move(50, 220)
        txtType = QLineEdit(self)
        txtType.move(50, 255)
        txtType.resize(250, 30)

        btnSubmit = QPushButton(self)
        btnSubmit.setText("Submit")
        btnSubmit.move(50, 320) 
        btnSubmit.resize(250, 50)

        # This needs to be an anonymous function for the signal to work
        btnSubmit.clicked.connect(lambda: controller.addField(txtClassName.text(), txtFieldName.text(), txtType.text()))

        self.exec_()

    # TODO: right now this takes the information entered into the menu and prints the data.
    # This information needs to be sent to the controller instead of being printed
    def addFieldData(self, className, fieldName, typ):
        self.close()
        print(className)
        print(fieldName)
        print(typ)

    def deleteField(self, controller):
        self.setWindowTitle('Delete Field')
        # w, h
        self.setFixedSize(350, 335)
        self.setStyleSheet(open('MenuStyleSheet.css').read()) 
        self.setModal(True)

        lblClassName = QLabel("Class Name", parent = self)
        lblClassName.move(50, 50)
        txtClassName = QLineEdit(self)
        txtClassName.move(50, 85)
        txtClassName.resize(250, 30)

        lblFieldName = QLabel("Field Name", parent = self)
        lblFieldName.move(50, 135)
        txtFieldName = QLineEdit(self)
        txtFieldName.move(50, 170)
        txtFieldName.resize(250, 30)

        btnSubmit = QPushButton(self)
        btnSubmit.setText("Submit")
        btnSubmit.move(50, 235) 
        btnSubmit.resize(250, 50)

        # Signal for Method Menu
        btnSubmit.clicked.connect(lambda: controller.deleteField(txtClassName.text(), txtFieldName.text()))

        self.exec_()

    def delFieldData(self, className, fieldName):
        self.close()
        print(className)
        print(fieldName)

    def renameField(self, controller):
        self.setWindowTitle('Rename Field')
        # w, h
        self.setFixedSize(350, 405)
        self.setStyleSheet(open('MenuStyleSheet.css').read()) 
        self.setModal(True)

        lblClassName = QLabel("Class Name", parent = self)
        lblClassName.move(50, 50)
        txtClassName = QLineEdit(self)
        txtClassName.move(50, 85)
        txtClassName.resize(250, 30)

        lblOldName = QLabel("Old Field Name", parent = self)
        lblOldName.move(50, 135)
        txtOldName = QLineEdit(self)
        txtOldName.move(50, 170)
        txtOldName.resize(250, 30)

        lblNewName = QLabel("New Field Name", parent = self)
        lblNewName.move(50, 220)
        txtNewName = QLineEdit(self)
        txtNewName.move(50, 255)
        txtNewName.resize(250, 30)

        btnSubmit = QPushButton(self)
        btnSubmit.setText("Submit")
        btnSubmit.move(50, 320) 
        btnSubmit.resize(250, 50)

        # This needs to be an anonymous function for the signal to work
        btnSubmit.clicked.connect(lambda: controller.renameField(txtClassName.text(), txtOldName.text(), txtNewName.text()))

        self.exec_()

    def renFieldData(self, className, oldName, newName):
        self.close()
        print(className)
        print(oldName)
        print(newName)

    