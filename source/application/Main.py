# Library Imports
import cv2
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage
# Internal modules import
import Config as APP_CONFIG
from Visualizer import *
from UI_Layout import *
from UI_Dialog import *
# Image processing files
import VehicleDetection as vd
import LaneDetection as ld

class ImageLoader(UI,Ui_Dialog):
    def __init__(self,MainWindow):
        UI.__init__(self,MainWindow)
        # Signals for push buttons
        self.loadImage.clicked.connect(self.getImage) 
        self.analyseImage.clicked.connect(self.processImage)
        # Signals for menu items
        self.actionImport_Image.triggered.connect(self.getImage)
        self.actionExport_Image.triggered.connect(self.saveImage)
        self.actionExit.triggered.connect(self.exitApp)    

        self.actionDetect_Vehicles.triggered.connect(self.detectVehicles)
        self.actionDetect_Lanes.triggered.connect(self.detectLanes)

    def displayStatus(self,statusMessage):
        MainWindow.statusBar().showMessage(statusMessage)

    def getImage(self):
        self.fname = QtWidgets.QFileDialog.getOpenFileName(MainWindow, 'Open file','E:\\', "Image files (*.jpg *.gif)")
        try:
            self.imagePath = self.fname[0]
            self.image = cv2.imread(self.imagePath)

            #Read metadata from the image
            status = Visualisor.LoadMetadata(self, self.imagePath)
            if status !=True: # Meta data not read
                if self.displayImageFromArray(self.image): #Image displayed on the canvas
                    self.displayStatus("Image loaded and ready for analysis, Error(s) encountered while reading exif-data from image: " + status)
                else: # image not displayed on the canvas
                    self.displayStatus("Unable to load the image. ")
            else: # Meta data read successfully
                self.displayImageFromArray(self.image)      
                self.displayStatus('Image loaded and ready for analysis...')
                return True
        except Exception as e:
            print(str(e))
            self.displayStatus('Error loading image.')

    def displayImageFromArray(self,img):
        print("INFO: MAIN: Drawing image on canvas.")
        try:
            height, width, channel = img.shape
            bytesPerLine = 3 * width
            #Create a QImage object from the numpy image array
            qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
            #Create a QPixmap to be displayed on the label widget
            pixMap = QtGui.QPixmap.fromImage(qImg)
            pix = QtGui.QPixmap(qImg)
            pix = pixMap.scaledToWidth(APP_CONFIG.IMG_WIDTH*1.5)
            #self.label.setGeometry(QtCore.QRect(APP_CONFIG.IMG_X,APP_CONFIG.IMG_Y, APP_CONFIG.IMG_WIDTH,APP_CONFIG.IMG_HEIGHT))
            self.label.setPixmap(pix)
            print("INFO: MAIN: Done!")
            return True
        except Exception as e:
            print(str(e)) 
            return False

    def detectLanes(self):
        try:
            # Read image from the selected path
            img = self.image
            self.displayStatus('Starting image analysis - Lane Detection...')
            # Perfome detection operation
            procImg,laneCoordinates = ld.detectLanesWhite(img)
            if laneCoordinates != False:
                laneMid =laneCoordinates
            else:
                pass
            print(laneMid)
            # Make a copy of the image
            self.image = procImg
            # Display processed image on canvas
            self.displayImageFromArray(procImg)
            self.displayStatus('Lane detection completed.')
        except Exception as e:
            print(str(e))
            self.displayStatus('Lane detection couldn\'t be completed.')
    
    def detectVehicles(self):
        try:
            # Read image from the selected path
            img = self.image
            self.displayStatus('Starting image analysis - Vehicle Detection...')
            # Perfome detection operation
            procImg,vehicleMetaData = vd.detectVehicles(img)
            # Make a copy of the image 
            self.image = procImg
            # Display processed image on canvas
            self.displayImageFromArray(procImg)
            self.displayStatus('Lane detection completed.')
        except Exception as e:
            print(str(e))
            self.displayStatus('Vehicle detection couldn\'t be completed.')

    def processImage(self):
        try:
            # Make a copy of the original image
            img = self.image
            print("INFO: MAIN: Image read for analysis.")
            print("INFO: MAIN: Processing image...")
            self.displayStatus('Starting image analysis...')
            # Perform detections
            procImg,laneCoordinates = ld.detectLanesWhite(img)
            procImg,vehicleMetaData = vd.detectVehicles(procImg)
            print("INFO: MAIN: Analysis done!")
            print("Lane Data:")
            print(laneCoordinates)
            print("Vehicle Data:")
            print(vehicleMetaData)
            self.displayStatus('Image analysis finished.')
            # Update the original image with the processed image
            self.image = procImg
            self.displayImageFromArray(procImg)
            print("INFO: MAIN: Process finished.")
            self.displayStatus('Image analysis results on canvas.')
            return True
        except Exception as e:
            print("ERROR: MAIN:" + str(e))
            self.displayStatus('Error(s) encountered while processing image.')
            return False

    def saveImage(self):
        try:
            fname = QtWidgets.QFileDialog.getSaveFileName(MainWindow, 'Save file','VEDD_outImage', "Image files (*.jpg)")
            filePath = fname[0]+".jpg"
            cv2.imwrite(filePath,self.image)
            self.displayStatus('File saved: ' + filePath)
        except Exception as e:
            print(str(e))
            self.displayStatus('Error(s) encountered while saving image.')
            return False
        
    # Exit application
    def exitApp(self):
        sys.exit()

if __name__ == "__main__":
    import sys
    # os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "0"
    app = QtWidgets.QApplication(sys.argv)
    # app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True) #enable highdpi scaling
    # app.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True) #use highdpi icons
    MainWindow = QtWidgets.QMainWindow()
    im = ImageLoader(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())