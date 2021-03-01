from PyQt5.QtWidgets import QWidget

class ParameterMenu(QWidget):
        
    def __init__(self, parent = None):
        super(ParameterMenu, self).__init__(parent)

        self.setWindowTitle('Add Parameter')
        self.resize(800, 800)
        self.setStyleSheet(open('GuiStyleSheet.css').read()) 