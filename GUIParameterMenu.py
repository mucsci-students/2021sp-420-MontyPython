# Contains classes used to create menus related to parameters

from PyQt5.QtWidgets import QWidget, QDialog, QLabel, QPushButton, QLineEdit

# This is the main parameter class. This adds/removes parameters by having the class and method passed in.
class ParameterMenu(QDialog):
        
    def __init__(self, parent = None):
        super(ParameterMenu, self).__init__(parent)

    # Creates a menu that requires a class name and method name
    def addParameter(self, controller):
        self.setWindowTitle('Add Parameter')
        # w, h
        self.setFixedSize(350, 505)
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

        lblParamName = QLabel("Parameter Name", parent = self)
        lblParamName.move(50, 220)
        txtParamName = QLineEdit(self)
        txtParamName.move(50, 255)
        txtParamName.resize(250, 30)

        lblParamType = QLabel("Parameter Type", parent = self)
        lblParamType.move(50, 305)
        txtParamType = QLineEdit(self)
        txtParamType.move(50, 340)
        txtParamType.resize(250, 30)

        btnSubmit = QPushButton(self)
        btnSubmit.setText("Submit")
        btnSubmit.move(50, 405) 
        btnSubmit.resize(250, 50)

        # This needs to be an anonymous function for the signal to work
        btnSubmit.clicked.connect(lambda: controller.addParameter(txtClassName.text(), txtMethodName.text(), txtParamName.text(), txtParamType.text()))

        self.exec_()

    # TODO: right now this takes the information entered into the menu and prints the data.
    # This information needs to be sent to the controller instead of being printed
    def addParamData(self, className, methodName, paramName, paramType):
        self.close()
        print(className)
        print(methodName)
        print(paramName)
        print(paramType)

    def deleteParameter(self, controller):
        self.setWindowTitle('Delete Parameter')
        # w, h
        self.setFixedSize(350, 405)
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

        lblParamName = QLabel("Parameter Name", parent = self)
        lblParamName.move(50, 220)
        txtParamName = QLineEdit(self)
        txtParamName.move(50, 255)
        txtParamName.resize(250, 30)

        btnSubmit = QPushButton(self)
        btnSubmit.setText("Submit")
        btnSubmit.move(50, 320) 
        btnSubmit.resize(250, 50)

        # This needs to be an anonymous function for the signal to work
        btnSubmit.clicked.connect(lambda: controller.deleteParameter(txtClassName.text(), txtMethodName.text(), txtParamName.text()))

        self.exec_()

    # TODO: right now this takes the information entered into the menu and prints the data.
    # This information needs to be sent to the controller instead of being printed
    def delParamData(self, className, methodName, paramName):
        self.close()
        print(className)
        print(methodName)
        print(paramName)

    # TODO change to changeParameter
    def changeParameter(self, controller):
        self.setWindowTitle('Change Parameter')
        # w, h
        self.setFixedSize(350, 590)
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

        lblOldName = QLabel("Old Parameter Name", parent = self)
        lblOldName.move(50, 220)
        txtOldName = QLineEdit(self)
        txtOldName.move(50, 255)
        txtOldName.resize(250, 30)

        lblParamType = QLabel("New Parameter Type", parent = self)
        lblParamType.move(50, 305)
        txtParamType = QLineEdit(self)
        txtParamType.move(50, 340)
        txtParamType.resize(250, 30)

        lblNewName = QLabel("New Parameter Name", parent = self)
        lblNewName.move(50, 390)
        txtNewName = QLineEdit(self)
        txtNewName.move(50, 425)
        txtNewName.resize(250, 30)

        btnSubmit = QPushButton(self)
        btnSubmit.setText("Submit")
        btnSubmit.move(50, 490) 
        btnSubmit.resize(250, 50)

        # This needs to be an anonymous function for the signal to work
        btnSubmit.clicked.connect(lambda: controller.changeParameter(txtClassName.text(), txtMethodName.text(), txtOldName.text(), txtParamType.text(), txtNewName.text()))

        self.exec_()

    # TODO: right now this takes the information entered into the menu and prints the data.
    # This information needs to be sent to the controller instead of being printed
    def renParamData(self, className, methodName, oldName, newType, newName):
        self.close()
        print(className)
        print(methodName)
        print(oldName)
        print(newType)
        print(newName)

# Creates a menu that works with Method Menu's add method. Does not require a class or method to be input
class MethodParameterMenu(QDialog):
        
    def __init__(self, paramTable, parent = None):
        super(ParameterMenu, self).__init__(parent)
        self.paramTable = paramTable

    def addParameterWithMethod(self):
        self.setWindowTitle('Add Parameter')
        # w, h
        self.setFixedSize(350, 335)
        self.setStyleSheet(open('MenuStyleSheet.css').read()) 
        self.setModal(True)

        lblParameterName = QLabel("Parameter Name", parent = self)
        lblParameterName.move(50, 50)
        txtParameterName = QLineEdit(self)
        txtParameterName.move(50, 85)
        txtParameterName.resize(250, 30)

        lblParameterType = QLabel("Parameter Type", parent = self)
        lblParameterType.move(50, 135)
        txtParameterType = QLineEdit(self)
        txtParameterType.move(50, 170)
        txtParameterType.resize(250, 30)

        btnSubmit = QPushButton(self)
        btnSubmit.setText("Submit")
        btnSubmit.move(50, 235) 
        btnSubmit.resize(250, 50)

        # Signal for Method Menu
        btnSubmit.clicked.connect(lambda: self.returnParam(txtParameterName.text(), txtParameterType.text()))

        self.exec_()

    # TODO: This is broken
    def returnParam(self, paramName, paramType):
        self.close()
        
        # TODO: Connect this back to previous menu somehow
        # Adds row to the end of the table
        rowCount = self.paramTable.rowCount()
        self.paramTable.insertRow(rowCount)

        # Populate the newly created row
        self.paramTable.setItem(rowCount, 0, QTableWidgetItem(paramName))
        self.paramTable.setItem(rowCount, 1, QTableWidgetItem(paramType))

    


