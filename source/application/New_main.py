from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import os
import Config as APP_CONFIG
from Visualizer import *
from UI_Layout import *
from PyQt5.QtGui import QImage
from ui_Dialog import *

class ImageLoader(UI,Ui_Dialog):
    def __init__(self,MainWindow):
        UI.__init__(self,MainWindow)
        self.title          =   APP_CONFIG.MAIN_WINDOW_TITLE
        self.left           =   APP_CONFIG.LEFT
        self.top            =   APP_CONFIG.TOP
        self.width          =   APP_CONFIG.WIDTH
        self.height         =   APP_CONFIG.HEIGHT
        self.img_resolution = (APP_CONFIG.WIDTH, APP_CONFIG.HEIGHT)
        self.loadImage.clicked.connect(self.getImage) 

    def displayStatus(self,statusMessage):
        MainWindow.statusBar().showMessage(statusMessage)

    def getImage(self):
        self.fname = QtWidgets.QFileDialog.getOpenFileName(MainWindow, 'Open file','C:\\', "Image files (*.jpg *.gif)")
        try:
            self.imagePath = self.fname[0]
            self.img = cv2.imread(self.imagePath)
            self.img = cv2.resize(self.img, self.img_resolution )
            Visualisor.getImagePath(self, self.imagePath)
            status = Visualisor.LoadMetadata(self, self.imagePath)
            if status !=True:
                self.displayStatus("ERROR: Unable to read meta-data from image: " + status)
            # Visualisor.one(self)
            self.displayImageFromArray()      
            return True
        except Exception as e:
            print(str(e))
            return False
    def displayImageFromArray(self):
        print("INFO: MAIN: Drawing image on canvas.")
        try:
            pixmap = QtGui.QPixmap(self.imagePath)
            height, width, channel = self.img.shape
            bytesPerLine = 3 * width
            #Create a QImage object from the numpy image array
            qImg = QImage(self.img.data, width, height, bytesPerLine, QImage.Format_RGB888)
            #Create a QPixmap to be displayed on the label widget
            pix = QtGui.QPixmap(qImg)
            pix = pixmap.scaledToWidth(APP_CONFIG.IMG_WIDTH*1.5)
            self.label.setGeometry(QtCore.QRect(APP_CONFIG.IMG_X,APP_CONFIG.IMG_Y, APP_CONFIG.IMG_WIDTH,APP_CONFIG.IMG_HEIGHT))
            self.label.setPixmap(pix)
            print("INFO: MAIN: Done!")
            return True
        except Exception as e:
            print(str(e)) 
            return False

        
        
if __name__ == "__main__":
    import sys
    # os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QtWidgets.QApplication(sys.argv)
    app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True) #enable highdpi scaling
    app.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True) #use highdpi icons
    MainWindow = QtWidgets.QMainWindow()
    im = ImageLoader(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())