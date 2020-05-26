# Importing required libraries
import cv2
import sys 
import os
from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import QAction,QMenu
# Configuration module
import Config as APP_CONFIG
# UI files
from Visaulizor import *
from UI import *
from ui_Dialog import *
# Image processing files
import VehicleDetection as vd
import LaneDetection as ld


class Ui_MainWindow(object): 
    def __init__(self):
        super().__init__()
        self.title          =   APP_CONFIG.MAIN_WINDOW_TITLE
        self.left           =   APP_CONFIG.LEFT
        self.top            =   APP_CONFIG.TOP
        self.width          =   APP_CONFIG.WIDTH
        self.height         =   APP_CONFIG.HEIGHT
        self.img_resolution = (APP_CONFIG.IMG_WIDTH, APP_CONFIG.IMG_HEIGHT)
    def displayStatus(self,statusMessage):
        MainWindow.statusBar().showMessage(statusMessage)

    def setupUi(self, MainWindow): 
        MainWindow.setWindowTitle(self.title)
        MainWindow.setGeometry(self.left, self.top, self.width, self.height)
        #Fix window size so maximizing does not distort the layout.
        MainWindow.setFixedSize(self.width, self.height)
        self.centralwidget = QtWidgets.QWidget(MainWindow) 
        
        # Add push-buttons to the UI  
        ## pushbutton for loading data
        self.btn_loadData = QtWidgets.QPushButton(self.centralwidget)
        self.alignButton(self.btn_loadData,520, 10,APP_CONFIG.LOAD_DATA) 
        self.btn_loadData.setToolTip("Load image for analysis")
        ## pushbutton for analysing image
        self.btn_analyseData = QtWidgets.QPushButton(self.centralwidget)
        self.alignButton(self.btn_analyseData,520, 120,APP_CONFIG.PROCESS_IMAGE) 
        self.btn_analyseData.setToolTip("Start image analysis")
        ## pushbutton for saving image
        self.btn_saveData = QtWidgets.QPushButton(self.centralwidget)
        self.alignButton(self.btn_saveData,520, 230,APP_CONFIG.SAVE_DATA) 
        self.btn_saveData.setToolTip("Save image to disk")
        ## add signals for the buttons  
        self.btn_loadData.clicked.connect(self.getImage) 
        self.btn_analyseData.clicked.connect(self.processImage)   
        self.btn_saveData.clicked.connect(self.saveImage)  

        # Add label to hold and display the image
        self.label = QtWidgets.QLabel(self.centralwidget) 
        self.label.setGeometry(QtCore.QRect(APP_CONFIG.IMG_X,APP_CONFIG.IMG_Y, APP_CONFIG.IMG_WIDTH,APP_CONFIG.IMG_HEIGHT))
        self.label.setToolTip("Image will be displayed here with a pre-set resolution, saved image will have the same resolution as that of the input image.")       
        # The set for the label is set to empty for now.
        self.label.setText("Select an Image.")  
        self.label.setFrameShape(QtWidgets.QFrame.Panel)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)

        # Add and display a message on a status-bar.
        self.displayStatus('Ready...')

        # Add a menu-bar
        menubar = MainWindow.menuBar()
        fileMenu = menubar.addMenu('File')
        toolsMenu = menubar.addMenu('Tools')
        helpMenu = menubar.addMenu("Help")

        # sub menus
        loadImage_menu  = QAction('Import Image', menubar)  
        saveImage_menu  =  QAction('Export Image', menubar) 
        exit_menu  =  QAction('Exit', menubar)

        detVehicles_menu = QAction('Detect Vehicels', menubar) 
        detLanes_menu = QAction('Detect Lanes', menubar) 
        detectionAnalysis_menu = QAction('Analyse Detections', menubar) 

        docLink_menu    = QAction("Documentation",menubar)
        about_menu      = QAction("About",menubar)

        # register sub-menus with the main menu-bar     
        fileMenu.addAction(loadImage_menu)
        fileMenu.addAction(saveImage_menu)
        fileMenu.addAction(exit_menu)

        toolsMenu.addAction(detVehicles_menu)
        toolsMenu.addAction(detLanes_menu)
        toolsMenu.addAction(detectionAnalysis_menu)

        # add signals to menu items
        loadImage_menu.triggered.connect(self.getImage)
        saveImage_menu.triggered.connect(self.saveImage)
        exit_menu.triggered.connect(self.exitApp)

        detVehicles_menu.triggered.connect(self.detectVehicles)
        detLanes_menu.triggered.connect(self.detectLanes)
        detectionAnalysis_menu.triggered.connect(self.processImage)

        helpMenu.addAction(docLink_menu)
        helpMenu.addAction(about_menu)
        ####

    
        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow) 
  
    def alignButton(self,qtPushButton,x,y,caption):
        qtPushButton.setGeometry(QtCore.QRect(x, y, APP_CONFIG.BTN_WIDTH, APP_CONFIG.BTN_HEIGHT)) 
        qtPushButton.setText(caption)
        return True

    # This function aligns the UI to the center of the screen
    def centerWindow():
        qtRectangle = self.frameGeometry()
        print(str(qtRectangle))
        centerPoint = QDesktopWidget().availableGeometry().center() 
        qtRectangle.moveCenter(centerPoint)
        MainWindow.move(qtRectangle.topLeft())
        return True

    # Exit application
    def exitApp(self):
        sys.exit()

    # This function acts as the slot for the button click signal
    # It opens up a window to select the image file that needs to be loaded into the application
    def getImage(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(MainWindow, 'Open file','c:\\', "Image files (*.jpg *.gif)")
        try:
            self.imagePath = fname[0]
            self.image = cv2.imread(self.imagePath)
            height, width, channels = self.image.shape
            print("Resolution: " + str(height)+", " + str(width))
            #resize image
            self.displayImageFromArray(self.image)
            self.displayStatus('Image loaded and ready for analysis. Image resolution: '+ str(height)+" x " + str(width))
            return True
        except Exception as e:
            print(str(e))
            self.displayStatus('Error loading image.')
            return False

    def detectLanes(self):
        try:
            # Read image from the selected path
            img = self.image
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
  
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)  
    
    MainWindow = QtWidgets.QMainWindow()  
    ui = Ui_MainWindow()  
    ui.setupUi(MainWindow)  
    MainWindow.show() 
   
    sys.exit(app.exec_())  
