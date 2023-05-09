from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from un import Ui_MainWindow

# Create aplication
app = QtWidgets.QApplication(sys.argv)

# Create from and init UI
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

# Hook Logic
def buttonPress():
    ui.lineEdit.setText("\"Fuck\" YOU!")

ui.B2.clicked.connect(buttonPress)

# Run main loop 
sys.exit(app.exec_())