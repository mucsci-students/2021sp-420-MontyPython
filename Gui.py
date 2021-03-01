from PyQt5.QtWidgets import QApplication
import sys
import GUIView
# QApplication instance, pass in sys.argv because it deals with common command line args
qApp = QApplication(sys.argv)
window = GUIView.MainWindow()
window.show()

# Run the event loop
sys.exit(qApp.exec_())