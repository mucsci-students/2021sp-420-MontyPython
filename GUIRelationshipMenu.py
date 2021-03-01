from PyQt5.QtWidgets import QWidget

class RelationshipMenu(QWidget):
        
    def __init__(self, parent = None):
        super(RelationshipMenu, self).__init__(parent)

        self.setWindowTitle('Add Relationship')
        self.resize(400, 800)
        self.setStyleSheet(open('GuiStyleSheet.css').read()) 