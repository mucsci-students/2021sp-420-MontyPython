from PyQt5.QtWidgets import QWidget

class MethodMenu(QWidget):
        
    def __init__(self, parent = None):
        super(MethodMenu, self).__init__(parent)

        self.setWindowTitle('Add Method')
        self.resize(800, 800)
        self.setStyleSheet(open('GuiStyleSheet.css').read()) 