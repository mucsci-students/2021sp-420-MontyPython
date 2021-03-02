from PyQt5.QtWidgets import QWidget, QDialog

class ParameterMenu(QDialog):
        
    def __init__(self, parent = None):
        super(ParameterMenu, self).__init__(parent)

    def addParameter(self):
        self.setWindowTitle('Add Parameter')
        self.setFixedSize(600, 600)
        self.setStyleSheet(open('GuiStyleSheet.css').read()) 
        self.setModal(True)

        self.exec_()