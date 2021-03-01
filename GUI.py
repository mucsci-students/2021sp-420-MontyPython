from PyQt5.QtWidgets import QApplication
import sys
import GUIMainWindow
# QApplication instance, pass in sys.argv because it deals with common command line args
qApp = QApplication(sys.argv)
window = GUIMainWindow.MainWindow()
window.show()

# Run the event loop
sys.exit(qApp.exec_())
