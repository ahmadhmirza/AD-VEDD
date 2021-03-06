# Library Imports
import cv2
import os
from pathlib import Path
import json
import csv
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

from PyQt5.Qt import QApplication, QUrl, QDesktopServices
import sys

class ImageLoader(UI,Ui_Dialog):
    def __init__(self,MainWindow):
        UI.__init__(self,MainWindow)
        # Signals for push buttons
        self.loadImage.clicked.connect(self.getImage) 
        self.analyseImage.clicked.connect(self.processImage)
        self.loadVideo.clicked.connect(self.getVideo)
        self.analyseVideo.clicked.connect(self.processVideo)
        self.generateReport.clicked.connect(self.generateReport_File)
        # Signals for menu items
        self.actionImport_Image.triggered.connect(self.getImage)
        self.actionExport_Image.triggered.connect(self.saveImage)
        self.actionExit.triggered.connect(self.exitApp) 
        self.actionDocumentation.triggered.connect(self.openDoc) 
        self.actionRepository.triggered.connect(self.openRepo) 

        self.actionDetect_Vehicles.triggered.connect(self.detectVehicles)
        self.actionDetect_Lanes.triggered.connect(self.detectLanes)

        self.analysisResults={}

    #displayes a string message in the status bar
    def displayStatus(self,statusMessage):
        MainWindow.statusBar().showMessage(statusMessage)
    
    #Opens the URL of the documentation on the repo in a web-browser
    def openDoc(self):
        #app = QApplication(sys.argv)
        url = QUrl("https://github.com/ahmadhmirza/AD-VEDD/blob/dev-chkpoint/README.md")
        QDesktopServices.openUrl(url)

    #Opens the URL of the repo in a web-browser
    def openRepo(self):
        #app = QApplication(sys.argv)
        url = QUrl("https://github.com/ahmadhmirza/AD-VEDD")
        QDesktopServices.openUrl(url)

    #Function to load an image from the disk
    def getImage(self):
        self.fname, _ = QtWidgets.QFileDialog.getOpenFileName(MainWindow, 'Open file','E:\\', "Image files (*.jpg *.gif)")
        self.filename = Path(self.fname).name
        temp = self.filename.split(".", 1) 
        self.filename = temp[0]
        try:
            self.imagePath = self.fname
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

    #function to save the analysis report as a csv file
    def generateReport_File(self):
        try:
            fileName = self.filename
            fileName = "VEDD_analysis_report_"+ fileName
            fname = QtWidgets.QFileDialog.getSaveFileName(MainWindow, 'Save Report',fileName, "csv files (*.csv)")
            filePath = fname[0]+".csv"  
            with open(filePath, 'w') as f:
                for key in self.analysisResults.keys():
                    f.write("%s,%s\n"%(key,self.analysisResults[key]))
            self.displayStatus('Report is generated sucessfully at location: ' + filePath)                    
        except Exception as e:
            print (str(e))
            self.displayStatus('Error(s) While generating report.')

    #Function to load a video file from the disk   
    def getVideo(self):
        self.fname, _ = QtWidgets.QFileDialog.getOpenFileName(MainWindow, 'Open file','C:\\', "Video files (*.mp4)")
        self.filename = Path(self.fname).name
        temp = self.filename.split(".", 1) 
        self.filename = temp[0]
        try:
            self.videoPath = self.fname
            cap = cv2.VideoCapture(self.videoPath)
            self.videoArray = []
            if (cap.isOpened()== False): 
                print("Error opening video.")
                # Read until video is completed
            frameCount = 0
            while(cap.isOpened()):
                # Capture frame-by-frame
                ret, frame = cap.read()
                if ret == True:
                    # Display the resulting frame
                    self.videoArray.append(frame)
                    frameCount += 1
                    print("frames read: " + str(frameCount))
                # Break the loop
                else: 
                    break
            # When everything done, release the video capture object
            cap.release()
            # Closes all the frames
            cv2.destroyAllWindows()
            print("Total Frames: " + str(len(self.videoArray)))
            self.initVideoDisplay(self.videoArray[0])
        except Exception as e:
            print(str(e))
    
    #TODO: function to process each frame in the video and save in a list
    def processVideo(self):
        try:
            self.processed_videoArray = []
            print("INFO: MAIN: Processing Video frame by frame...")
            self.displayStatus('Processing Video frame by frame...')
            totalFrame = len(self.videoArray)
            print(totalFrame)
            count = 0

            for frame in self.videoArray :
                #procImg,laneCoordinates = ld.detectLanesWhite(frame)
                #procImg,vehicleMetaData = vd.detectVehicles(procImg)
                self.initVideoDisplay(frame)
                cv2.waitKey(25)
                #self.processed_videoArray.append(procImg)
                count += 1
                #self.displayStatus('Frame processed: ' + str(count) + "/" + str(totalFrame))
            self.displayStatus("Finished procesing all frames: " + str(totalFrame))
            return True
        except Exception as e:
            print("ERROR: MAIN:"+ str(e))
            self.displayStatus('Error(s) encountered while processing video frames.')
            return False

    #TODO: function to play the video on the canvas frame by frame
    def initVideoDisplay(self,firstFrame):
        try:
            height, width, channel = firstFrame.shape
            bytesPerLine = 3 * width
            #Create a QImage object from the numpy image array
            qImg = QImage(firstFrame.data, width, height, bytesPerLine, QImage.Format_RGB888)
            #Create a QPixmap to be displayed on the label widget
            pixMap = QtGui.QPixmap.fromImage(qImg)
            pix = QtGui.QPixmap(qImg)
            pix = pixMap.scaledToWidth(APP_CONFIG.IMG_WIDTH*1.5)
            #self.label.setGeometry(QtCore.QRect(APP_CONFIG.IMG_X,APP_CONFIG.IMG_Y, APP_CONFIG.IMG_WIDTH,APP_CONFIG.IMG_HEIGHT))
            self.videoCanvas.setPixmap(pix)
            return True
        except Exception as e:
            print(str(e)) 
            return False  
    #draws an image on the image canvas(label)
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

    #processes the image and highlights the lane markings in the input image
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

    #processes the image and draws bounding boxes around the detected vehicles in the input image
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

    #perfome both lane and vehicle detection
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
            count = 0
            for item in vehicleMetaData:
                count += 1
                self.Label = "Vehicle_"+str(count)
                
                self.analysisResults[self.Label] = item
            
            self.analysisResults["Lane"] = {
                "x1":laneCoordinates[0],
                "y1":laneCoordinates[1],
                "x2":laneCoordinates[2],
                "y2":laneCoordinates[3]
            }
            print("INFO: MAIN: Analysis done!")
            print("Lane Data:")
            print(laneCoordinates)
            print("Vehicle Data:")
            print(vehicleMetaData)
            self.v_data = vehicleMetaData
            self.displayStatus('Image analysis finished.')
            # Update the original image with the processed image
            self.image = procImg
            self.displayImageFromArray(procImg)
            print("INFO: MAIN: Process finished.")
            self.displayStatus('Image analysis results on canvas.')
            print(self.analysisResults)
            self.fill_Analysis_table(self.Analysis_result, self.analysisResults)
            self.generateReport.setEnabled(True)
            return True
        except Exception as e:
            print("ERROR: MAIN:" + str(e))
            self.displayStatus('Error(s) encountered while processing image.')
            return False

    #Populate table with metadata
    def Analysis_table_item(self, item, value):
        item.setExpanded(True)
        if type(value) is dict:
            for key, val in sorted(value.items()):
                child = QtWidgets.QTreeWidgetItem()
                child.setText(0, str(key))
                item.addChild(child)
                self.Analysis_table_item(child, val)
        elif type(value) is list:
            for val in value:
                child = QtWidgets.QTreeWidgetItem()
                item.addChild(child)
                if type(val) is dict:      
                    child.setText(0, str(self.label))
                    self.Analysis_table_item(child, val)
                elif type(val) is list:
                    child.setText(0, '[list]')
                    self.Analysis_table_item(child, val)
                else:
                    child.setText(0, str(val))              
                child.setExpanded(True)
        else:
            child = QtWidgets.QTreeWidgetItem()
            child.setText(0, str(value))
            item.addChild(child)

    def fill_Analysis_table(self,widget, value):
        widget.clear()
        self.Analysis_table_item(widget.invisibleRootItem(), value)
    
    #Save image to disk
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