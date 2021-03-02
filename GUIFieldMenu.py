from PyQt5.QtWidgets import QWidget, QDialog, QLabel, QLineEdit, QPushButton

class FieldMenu(QDialog):
        
    def __init__(self, parent = None):
        super(FieldMenu, self).__init__(parent)

    def addField(self):
        self.setWindowTitle('Add Field')
        self.setFixedSize(350, 350)
        self.setStyleSheet(open('MenuStyleSheet.css').read()) 
        self.setModal(True)

        lblName = QLabel("Field Name", parent = self)
        lblName.move(50, 50)
        txtName = QLineEdit(self)
        txtName.move(50, 85)
        txtName.resize(250, 30)

        lblType = QLabel("Field Data Type", parent = self)
        lblType.move(50, 150)
        txtType = QLineEdit(self)
        txtType.move(50, 185)
        txtType.resize(250, 30)

        btnSubmit = QPushButton(self)
        btnSubmit.setText("Submit")
        btnSubmit.move(50, 260) 
        btnSubmit.resize(250, 50)

        self.exec_()