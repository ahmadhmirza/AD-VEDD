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

        ##### SIGNALS #####
        # Create a signal to detect a change in the title of the window
        # the signal is connected to the function in the parameters.
        # when ever the signla is detected the connected function will be called.
        self.windowTitleChanged.connect(self.onWindowTitleChange)

        ##### EVENTS #####



        #set window title
        self.setWindowTitle("Hello QT!")

        # create a qLabel
        label = QLabel("First PyQt app.")
        # align the widget to the center
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)
    
    #Slot for accepting the string passed from the signal on line 17
    def onWindowTitleChange(self,titleString):
        print(titleString)

    def contextMenuEvent(self, event):
        print("Right click on the window detected.")
        # To trigger the default event handler after custom actions have been performed:
        super(MainWindow, self).contextMenuEvent(event)

        # if the function has dealt with the event completly and there is no need to propagate it:
        event.accept()
        # to propagate to UI-parent-widget
        #event.ignore()


# Creating the Qapplication instance
app = QApplication(sys.argv)

# create an instance of the MainWindow
# should be done before entring the event loop

window = MainWindow()
window.show()


# start event loop
app.exec_()