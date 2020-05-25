from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import Config as APP_CONFIG
from Visaulizor import *
from UI import *
from PyQt5.QtGui import QImage

class ImageLoader(UI):
    def __init__(self,MainWindow):
        UI.__init__(self,MainWindow)
        self.title          =   APP_CONFIG.MAIN_WINDOW_TITLE
        self.left           =   APP_CONFIG.LEFT
        self.top            =   APP_CONFIG.TOP
        self.width          =   APP_CONFIG.WIDTH
        self.height         =   APP_CONFIG.HEIGHT
        self.img_resolution = (APP_CONFIG.WIDTH, APP_CONFIG.HEIGHT)
        self.loadImage.clicked.connect(self.getImage) 
    def getImage(self):
        self.fname = QtWidgets.QFileDialog.getOpenFileName(MainWindow, 'Open file','E:\\', "Image files (*.jpg *.gif)")
        try:
            self.imagePath = self.fname[0]
            self.img = cv2.imread(self.imagePath)
            self.img = cv2.resize(self.img, self.img_resolution )
            Visualisor.getImagePath(self, self.imagePath)
            Visualisor.LoadMetadata(self, self.imagePath)
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
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    im = ImageLoader(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())
