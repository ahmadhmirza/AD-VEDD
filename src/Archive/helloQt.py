import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import sys


# QMainWindow - parent class
class MainWindow(QMainWindow):
    #
    def __init__(self, *args,**kwargs):
        # always when sub-classing a qt-class a super init function must be called.
        super(MainWindow,self).__init__(*args,**kwargs)

        #set window title
        self.setWindowTitle("Hello QT!")

        # create a qLabel
        label = QLabel("First PyQt app.")
        # align the widget to the center
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)
        
# Creating the Qapplication instance
app = QApplication(sys.argv)

# create an instance of the MainWindow
# should be done before entring the event loop

window = MainWindow()
window.show()

# start event loop
app.exec_()