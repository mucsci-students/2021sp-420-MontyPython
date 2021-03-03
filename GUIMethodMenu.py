# Contains classes used to create menus related to methods

from PyQt5.QtWidgets import QWidget, QDialog, QTableWidget, QLabel, QLineEdit, QPushButton
import GUIParameterMenu

class MethodMenu(QDialog):
        
    def __init__(self, parent = None):
        super(MethodMenu, self).__init__(parent)

    def addMethod(self):
        self.setWindowTitle('Add Method')
        # w, h
        self.setFixedSize(602, 420)
        self.setStyleSheet(open('MenuStyleSheet.css').read()) 
        self.setModal(True)

        lblClassName = QLabel("Class Name", parent = self)
        lblClassName.move(50, 50)
        txtClassName = QLineEdit(self)
        txtClassName.move(50, 85)
        txtClassName.resize(250, 30)

        lblMethodName = QLabel("Method Name", parent = self)
        lblMethodName.move(50, 135)
        txtMethodName = QLineEdit(self)
        txtMethodName.move(50, 170)
        txtMethodName.resize(250, 30)

        lblType = QLabel("Method Return Type", parent = self)
        lblType.move(50, 220)
        txtType = QLineEdit(self)
        txtType.move(50, 255)
        txtType.resize(250, 30)

        btnSubmit = QPushButton(self)
        btnSubmit.setText("Submit")
        btnSubmit.move(50, 320) 
        btnSubmit.resize(250, 50)

        lblParams = QLabel("Parameters", parent = self)
        lblParams.move(350, 50)
        paramTable = QTableWidget(self)
        paramTable.setColumnCount(2)
        paramTable.setFixedSize(202, 200)
        paramTable.move(350, 85)
        paramTable.setHorizontalHeaderLabels(('Name', 'Type'))

        btnParams = QPushButton(self)
        btnParams.setText("Add Parameter")
        btnParams.move(350, 320) 
        btnParams.resize(202, 50)

        # This needs to be an anonymous function for the signal to work
        btnParams.clicked.connect(lambda: self.addParameterToTable(paramTable))
        btnSubmit.clicked.connect(lambda: self.addMethodData(txtClassName.text(), txtMethodName.text(), txtType.text(), "Loop through and add this"))

        self.exec_()

    # TODO: Unfinished. This does not work
    def addParameterToTable(self, checked, paramTable):
        self.pMenu = GUIParameterMenu.MethodParameterMenu(paramTable)
        self.pMenu.addParameterWithMethod()
    
    # TODO: right now this takes the information entered into the menu and prints the data.
    # This information needs to be sent to the controller instead of being printed
    def addMethodData(self, className, methodName, returnType, parameters):
        self.close()
        print(className)
        print(methodName)
        print(returnType)
        print(parameters)

    # TODO: This method does not include use input to ask for the parameters
    # I've been basing these off of the required input for our functions, so I'm not sure how this will work
    def deleteMethod(self):
        self.setWindowTitle('Delete Method')
        # w, h
        self.setFixedSize(350, 335)
        self.setStyleSheet(open('MenuStyleSheet.css').read()) 
        self.setModal(True)

        lblClassName = QLabel("Class Name", parent = self)
        lblClassName.move(50, 50)
        txtClassName = QLineEdit(self)
        txtClassName.move(50, 85)
        txtClassName.resize(250, 30)

        lblMethodName = QLabel("Method Name", parent = self)
        lblMethodName.move(50, 135)
        txtMethodName = QLineEdit(self)
        txtMethodName.move(50, 170)
        txtMethodName.resize(250, 30)

        btnSubmit = QPushButton(self)
        btnSubmit.setText("Submit")
        btnSubmit.move(50, 235) 
        btnSubmit.resize(250, 50)

        # This needs to be an anonymous function for the signal to work
        btnSubmit.clicked.connect(lambda: self.delMethodData(txtClassName.text(), txtMethodName.text()))

        self.exec_()

    # TODO: right now this takes the information entered into the menu and prints the data.
    # This information needs to be sent to the controller instead of being printed
    def delMethodData(self, className, methodName):
        self.close()
        print(className)
        print(methodName)

    def renameMethod(self):
        self.setWindowTitle('Rename Method')
        # w, h
        self.setFixedSize(350, 405)
        self.setStyleSheet(open('MenuStyleSheet.css').read()) 
        self.setModal(True)

        lblClassName = QLabel("Class Name", parent = self)
        lblClassName.move(50, 50)
        txtClassName = QLineEdit(self)
        txtClassName.move(50, 85)
        txtClassName.resize(250, 30)

        lblOldName = QLabel("Old Method Name", parent = self)
        lblOldName.move(50, 135)
        txtOldName = QLineEdit(self)
        txtOldName.move(50, 170)
        txtOldName.resize(250, 30)

        lblNewName = QLabel("New Method Name", parent = self)
        lblNewName.move(50, 220)
        txtNewName = QLineEdit(self)
        txtNewName.move(50, 255)
        txtNewName.resize(250, 30)

        btnSubmit = QPushButton(self)
        btnSubmit.setText("Submit")
        btnSubmit.move(50, 320) 
        btnSubmit.resize(250, 50)

        # This needs to be an anonymous function for the signal to work
        btnSubmit.clicked.connect(lambda: self.renMethodData(txtClassName.text(), txtOldName.text(), txtNewName.text()))

        self.exec_()

    # TODO: right now this takes the information entered into the menu and prints the data.
    # This information needs to be sent to the controller instead of being printed
    def renMethodData(self, className, oldName, newName):
        self.close()
        print(className)
        print(oldName)
        print(newName)

