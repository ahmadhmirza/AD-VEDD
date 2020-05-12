# from PyQt5 import QtGui
# from PyQt5.QtWidgets import QApplication, QVBoxLayout, QPushButton, QLabel
# from PyQt5.QtWidgets import QDesktopWidget,QWidget, QFileDialog, QTextEdit
# from PyQt5.QtCore import *
# from PyQt5.QtGui import QPixmap,QScreen

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import cv2
import Config as APP_CONFIG
import ImageAnalysis as imgAnalysis
from PyQt5.QtGui import QImage

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title  =   APP_CONFIG.MAIN_WINDOW_TITLE
        self.left   =   APP_CONFIG.LEFT
        self.top    =   APP_CONFIG.TOP
        self.width  =   APP_CONFIG.WIDTH
        self.height =   APP_CONFIG.HEIGHT
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.centerWindow()

        #The QVBoxLayout class lines up widgets vertically
        vbox = QVBoxLayout()

        # Add the button to browse for the image
        self.btn1 = QPushButton(APP_CONFIG.LOAD_DATA)
        self.btn1.clicked.connect(self.getImage)

        #Add a label where the image will be displayed
        self.label = QLabel("")
        
        #Add widgets to vbox
        vbox.addWidget(self.btn1)
        vbox.addWidget(self.label)

        self.setLayout(vbox)
        self.show()

    # This function aligns the UI to the center of the screen
    def centerWindow(self):
        qtRectangle = self.frameGeometry()
        print(str(qtRectangle))
        centerPoint = QDesktopWidget().availableGeometry().center() 
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

    # This function acts as the slot for the button click signal
    # It opens up a window to select the image file that needs to be loaded into the application
    def getImage(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file','c:\\', "Image files (*.jpg *.gif)")
        imagePath = fname[0]
        pixmap = QPixmap(imagePath)
        img = cv2.imread(imagePath)
        #resolution of the image to match the window size
        img_resolution = (APP_CONFIG.WIDTH, APP_CONFIG.HEIGHT)
        #resize image
        img = cv2.resize(img, img_resolution)
        #pass the image to ImageAnalysis module to detect objects and draw bounding boxes
        procImg = imgAnalysis.detectCarsAndLanes(img)
        height, width, channel = procImg.shape
        bytesPerLine = 3 * width
        #Create a QImage object from the numpy image array
        qImg = QImage(procImg.data, width, height, bytesPerLine, QImage.Format_RGB888)
        #Create a QPixmap to be displayed on the label widget
        pix = QPixmap(qImg)
        self.label.setPixmap(pix)
        self.resize(APP_CONFIG.WIDTH, APP_CONFIG.HEIGHT)
        self.centerWindow()

        #self.label.setPixmap(QPixmap(pixmap))
        #self.resize(pixmap.width(), pixmap.height())
        #self.centerWindow()
 
 
def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

if __name__ =="__main__":
    main()