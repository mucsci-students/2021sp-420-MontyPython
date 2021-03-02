from PyQt5.QtWidgets import QWidget, QDialog

class MethodMenu(QDialog):
        
    def __init__(self, parent = None):
        super(MethodMenu, self).__init__(parent)

    def addMethod(self):
        self.setWindowTitle('Add Method')
        self.setFixedSize(600, 600)
        #self.resize(600, 600)
        self.setStyleSheet(open('GuiStyleSheet.css').read()) 
        #self.setWindowFlags()
        self.setModal(True)
        self.exec_()