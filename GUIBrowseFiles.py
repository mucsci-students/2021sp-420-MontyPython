from PyQt5.QtWidgets import QFileDialog, QWidget

class BrowseFiles(QWidget):
        
    def __init__(self, parent = None):
        super(BrowseFiles, self).__init__(parent)

    def openFile(self):
        opt = QFileDialog.Options()
        # If _ is omitted, it'll save the path and 'All Files' which isn't necessary
        file, _ = QFileDialog.getOpenFileName(self,"Open File", options=opt)

        # TODO: This print statement needs to be changed to give info to the controller
        print(file) 

    def saveFile(self):
        opt = QFileDialog.Options()
        # If _ is omitted, it'll save the path and 'All Files' which isn't necessary
        file, _ = QFileDialog.getSaveFileName(self,"Save File", options=opt)

        # TODO: This print statement needs to be changed to give info to the controller
        print(file) 