from PyQt5.QtWidgets import QWidget, QDialog, QLabel, QLineEdit, QPushButton

class AlertWindow(QDialog):
        
    def __init__(self, parent = None):
        super(AlertWindow, self).__init__(parent)

    def addAlert(self, controller, e):
        self.setWindowTitle('ERROR')
        self.setFixedSize(350, 250)
        self.setStyleSheet(open('MenuStyleSheet.css').read())
        lblName = QLabel(f'Error: {e}', parent = self)
        lblName.move(50, 50)
        self.setModal(True)
        self.exec_()