from PyQt5.QtWidgets import QWidget, QDialog, QLabel, QLineEdit, QPushButton

class ClassMenu(QDialog):
        
    def __init__(self, parent = None):
        super(ClassMenu, self).__init__(parent)

    def addClass(self, controller):
        self.setWindowTitle('Add Class')
        self.setFixedSize(350, 250)
        self.setStyleSheet(open('MenuStyleSheet.css').read()) 
        self.setModal(True)

        lblName = QLabel("Class Name", parent = self)
        lblName.move(50, 50)
        txtName = QLineEdit(self)
        txtName.move(50, 85)
        txtName.resize(250, 30)

        btnSubmit = QPushButton(self)
        btnSubmit.setText("Submit")
        btnSubmit.move(50, 150) 
        btnSubmit.resize(250, 50)

        # This needs to be an anonymous function for the signal to work
        btnSubmit.clicked.connect(lambda: controller.addClass(txtName.text()))

        self.exec_()

    # TODO: right now this takes the information entered into the menu and prints the data.
    # This information needs to be sent to the controller instead of being printed
    def addClassData(self, name):
        self.close()
        print(name)

    def deleteClass(self, controller):
        self.setWindowTitle('Delete Class')
        self.setFixedSize(350, 250)
        self.setStyleSheet(open('MenuStyleSheet.css').read()) 
        self.setModal(True)

        lblName = QLabel("Class Name", parent = self)
        lblName.move(50, 50)
        txtName = QLineEdit(self)
        txtName.move(50, 85)
        txtName.resize(250, 30)

        btnSubmit = QPushButton(self)
        btnSubmit.setText("Submit")
        btnSubmit.move(50, 150) 
        btnSubmit.resize(250, 50)

        # This needs to be an anonymous function for the signal to work
        btnSubmit.clicked.connect(lambda: controller.deleteClass(txtName.text()))

        self.exec_()

    # TODO: right now this takes the information entered into the menu and prints the data.
    # This information needs to be sent to the controller instead of being printed
    def deleteClassData(self, name):
        self.close()
        print(name)

    def renameClass(self, controller):
        self.setWindowTitle('Rename Class')
        # w, h
        self.setFixedSize(350, 335)
        self.setStyleSheet(open('MenuStyleSheet.css').read()) 
        self.setModal(True)

        lblOldName = QLabel("Old Name", parent = self)
        lblOldName.move(50, 50)
        txtOldName = QLineEdit(self)
        txtOldName.move(50, 85)
        txtOldName.resize(250, 30)

        lblNewName = QLabel("New Name", parent = self)
        lblNewName.move(50, 135)
        txtNewName = QLineEdit(self)
        txtNewName.move(50, 170)
        txtNewName.resize(250, 30)

        btnSubmit = QPushButton(self)
        btnSubmit.setText("Submit")
        btnSubmit.move(50, 235) 
        btnSubmit.resize(250, 50)

        # Signal for Method Menu
        btnSubmit.clicked.connect(lambda: controller.renameClass(txtOldName.text(), txtNewName.text()))

        self.exec_()

    # TODO: right now this takes the information entered into the menu and prints the data.
    # This information needs to be sent to the controller instead of being printed
    def renameClassData(self, oldName, newName):
        self.close()
        print(oldName)
        print(newName)







    