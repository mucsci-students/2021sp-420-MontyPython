from PyQt5.QtWidgets import QWidget, QDialog

class ClassMenu(QDialog):
        
    def __init__(self, parent = None):
        super(ClassMenu, self).__init__(parent)

    def addClass(self):
        self.setWindowTitle('Add Class')
        self.setFixedSize(600, 600)
        #self.resize(600, 600)
        self.setStyleSheet(open('GuiStyleSheet.css').read()) 
        #self.setWindowFlags()
        self.setModal(True)
        self.exec_()







    