# Importing required libraries
import cv2
import sys 
import os
import VehicleDetection as vd
import LaneDetection as ld

def detectLanes(image):
    try:
        # Read image from the selected path
        img = image
        self.displayStatus('Starting image analysis - Lane Detection...')
        # Perfome detection operation
        procImg = ld.detectLanesWhite(img)
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
        procImg = vd.detectVehicles(img)
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

def displayImageFromArray(self,img):
    print("INFO: MAIN: Drawing image on canvas.")
    try:
        #change
        img = cv2.resize(img, self.img_resolution)
        pixmap = QtGui.QPixmap(self.imagePath)
        height, width, channel = img.shape
        bytesPerLine = 3 * width
        #self.displayStatus("Resized To: "+ str(height)+" x " + str(width))
        #Create a QImage object from the numpy image array
        qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
        #Create a QPixmap to be displayed on the label widget
        pix = QtGui.QPixmap(qImg)
        self.label.setPixmap(pix)
        MainWindow.resize(APP_CONFIG.WIDTH, APP_CONFIG.HEIGHT)
        #self.centerWindow()
        print("INFO: MAIN: Done!")
        return True
    except Exception as e:
        print(str(e)) 
        return False
