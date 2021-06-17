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
        #Add a label where the image will be displayed
        self.label = QLabel(self)
        self.label = QLabel("")
        self.label.setGeometry(APP_CONFIG.IMG_X, APP_CONFIG.IMG_Y, APP_CONFIG.IMG_WIDTH, APP_CONFIG.IMG_HEIGHT)
        # Add the button to browse for the image
        self.btn1 = QPushButton(APP_CONFIG.LOAD_DATA)
        self.btn1.clicked.connect(self.getImage)
        # Add the button to start the image analysis
        self.btn2 = QPushButton(APP_CONFIG.PROCESS_IMAGE)
        self.btn2.clicked.connect(self.processImage)

        #Add widgets to vbox
        vbox.addWidget(self.label)
        vbox.addWidget(self.btn1)
        vbox.addWidget(self.btn2)

        self.setLayout(vbox)
        self.show()

    def alignButtons(self,qtPushButton,x,y):
        qtPushButton.resize(APP_CONFIG.BTN_WIDTH,APP_CONFIG.BTN_HEIGHT)
        qtPushButton.move(x, y) 
        return True 

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
        try:
            self.imagePath = fname[0]
            img = cv2.imread(self.imagePath)
            img_resolution = (APP_CONFIG.WIDTH, APP_CONFIG.HEIGHT)
            #resize image
            img = cv2.resize(img, img_resolution)
            self.displayImageFromArray(img)
        except Exception as e:
            print(str(e))

    def processImage(self):
        try:
            img = cv2.imread(self.imagePath)
            print("DEBUG: Image read for analysis.")
            #resolution of the image to match the window size
            img_resolution = (APP_CONFIG.WIDTH, APP_CONFIG.HEIGHT)
            #resize image
            img = cv2.resize(img, img_resolution)
            #pass the image to ImageAnalysis module to detect objects and draw bounding boxes
            print("DEBUG: Processing image...")
            procImg = imgAnalysis.detectCarsAndLanes(img)
            print("DEBUG: Done!")
            procImg = cv2.resize(img, img_resolution)
            self.displayImageFromArray(procImg)
        except Exception as e:
            print("ERROR: " + str(e))


    def displayImageFromArray(self,img):
        print("Drawing image on canvas.")
        try:
            pixmap = QPixmap(self.imagePath)
            height, width, channel = img.shape
            bytesPerLine = 3 * width
            #Create a QImage object from the numpy image array
            qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
            #Create a QPixmap to be displayed on the label widget
            pix = QPixmap(qImg)
            self.label.setPixmap(pix)
            self.resize(APP_CONFIG.WIDTH, APP_CONFIG.HEIGHT)
            self.centerWindow()
            print("DEBUG: Done!")
        except Exception as e:
            print(str(e))
 
 
def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

if __name__ =="__main__":
    main()