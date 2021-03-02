from PyQt5.QtWidgets import QWidget, QDialog

class RelationshipMenu(QDialog):
        
    def __init__(self, parent = None):
        super(RelationshipMenu, self).__init__(parent)

    def addRelationship(self):
        self.setWindowTitle('Add Relationship')
        self.setFixedSize(600, 600)
        #self.resize(600, 600)
        self.setStyleSheet(open('GuiStyleSheet.css').read()) 
        #self.setWindowFlags()
        self.setModal(True)
        self.exec_()