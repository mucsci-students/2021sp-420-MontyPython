from PyQt5.QtWidgets import QWidget

class ClassMenu(QWidget):
        
    def __init__(self, parent = None):
        super(ClassMenu, self).__init__(parent)

        self.setWindowTitle('Add Class')
        self.resize(800, 800)
        self.setStyleSheet(open('GuiStyleSheet.css').read()) 







    