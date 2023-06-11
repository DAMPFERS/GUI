from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import sys
import csv_test
from menu_test import Ui_MainWindow

# Create aplication
app = QtWidgets.QApplication(sys.argv)

# Create from and init UI
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

# Hook Logic ##############################################################


def buttonOpenFile():
    #ui.buttonFile.setText("Fuck")
    res = QFileDialog.getOpenFileName(None, 'Open Image', '\\PROGRAMS\\NTO\\csv', 'CSV Files (*.csv)')
    byte = csv_test.csv_read(res[0])
    for i in range(8):
        c = byte[i][0]
        for j in range(7, -1, -1):
            if c % 2:
               ui.table.item(i,j).setText('1')
            else:
                ui.table.item(i,j).setText('0')
            c = c >> 1
    

ui.buttonFile.clicked.connect(buttonOpenFile)
 



# Run main loop ################################################
sys.exit(app.exec_())