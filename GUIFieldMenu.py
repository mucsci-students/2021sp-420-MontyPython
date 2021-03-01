from PyQt5.QtWidgets import QWidget

class FieldMenu(QWidget):
        
    def __init__(self, parent = None):
        super(FieldMenu, self).__init__(parent)

        self.setWindowTitle('Add Field')
        self.resize(800, 800)
        self.setStyleSheet(open('GuiStyleSheet.css').read()) 