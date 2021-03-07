# Contains classes used to create menus related to methods

from PyQt5.QtWidgets import QWidget, QDialog, QTableWidget, QTableWidgetItem, QLabel, QLineEdit, QPushButton
import GUIParameterMenu

class MethodMenu(QDialog):
        
    def __init__(self, parent = None):
        super(MethodMenu, self).__init__(parent)

        self.returnDict = {'Values Entered': False}

    def addMethod(self, controller):
        self.setWindowTitle('Add Method')
        # w, h
        self.setFixedSize(619, 420)
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
        self.paramTable = QTableWidget(self)
        self.paramTable.setColumnCount(2)
        self.paramTable.setFixedSize(219, 200)
        self.paramTable.move(350, 85)
        self.paramTable.setHorizontalHeaderLabels(('Name', 'Type'))

        btnParams = QPushButton(self)
        btnParams.setText("Add Parameter")
        btnParams.move(350, 320) 
        btnParams.resize(202, 50)

        # This needs to be an anonymous function for the signal to work
        btnParams.clicked.connect(lambda: self.addParameterToTable())
        btnSubmit.clicked.connect(lambda: controller.addMethod(txtClassName.text(), txtMethodName.text(), txtType.text(), "Loop through and add this"))

        self.exec_()

    # TODO: Unfinished. This does not work
    def addParameterToTable(self):
        self.pMenu = GUIParameterMenu.MethodParameterMenu(self.returnDict)
        self.pMenu.addParameterWithMethod()
        if self.returnDict['Values Entered'] == True:
            rowCount = self.paramTable.rowCount()
            self.paramTable.insertRow(rowCount)

            #Populate the newly created row
            self.paramTable.setItem(rowCount, 0, QTableWidgetItem(self.returnDict['Parameter Name']))
            self.paramTable.setItem(rowCount, 1, QTableWidgetItem(self.returnDict['Parameter Type']))
    
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
    def deleteMethod(self, controller):
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
        btnSubmit.clicked.connect(lambda: controller.deleteMethod(txtClassName.text(), txtMethodName.text()))

        self.exec_()

    # TODO: right now this takes the information entered into the menu and prints the data.
    # This information needs to be sent to the controller instead of being printed
    def delMethodData(self, className, methodName):
        self.close()
        print(className)
        print(methodName)

    def renameMethod(self, controller):
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
        btnSubmit.clicked.connect(lambda: controller.renameMethod(txtClassName.text(), txtOldName.text(), txtNewName.text()))

        self.exec_()

    # TODO: right now this takes the information entered into the menu and prints the data.
    # This information needs to be sent to the controller instead of being printed
    def renMethodData(self, className, oldName, newName):
        self.close()
        print(className)
        print(oldName)
        print(newName)

