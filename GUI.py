from PyQt5.QtWidgets import QApplication
import sys
import GUIMainWindow
import GUIController
import ClassCollection

# QApplication instance, pass in sys.argv because it deals with common command line args
model = ClassCollection.ClassCollection()
qApp = QApplication(sys.argv)
window = GUIMainWindow.MainWindow()
controller = GUIController.GUIController(model, window)

window.show()

# Run the event loop
sys.exit(qApp.exec_())
