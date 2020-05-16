
from PyQt5 import QtCore, QtGui, QtWidgets 

import sys 
import cv2
import Config as APP_CONFIG
import VehicleDetection as vd
import LaneDetection as ld
from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import QAction,QMenu

class Ui_MainWindow(object): 
    def __init__(self):
        super().__init__()
        self.title          =   APP_CONFIG.MAIN_WINDOW_TITLE
        self.left           =   APP_CONFIG.LEFT
        self.top            =   APP_CONFIG.TOP
        self.width          =   APP_CONFIG.WIDTH
        self.height         =   APP_CONFIG.HEIGHT
        self.img_resolution = (APP_CONFIG.WIDTH, APP_CONFIG.HEIGHT)
    def displayStatus(self,statusMessage):
        MainWindow.statusBar().showMessage(statusMessage)

    def setupUi(self, MainWindow): 
        MainWindow.setWindowTitle(self.title)
        MainWindow.setGeometry(self.left, self.top, self.width, self.height)
        #Fix window size so maximizing does not distort the layout.
        MainWindow.setFixedSize(self.width, self.height)
        self.centralwidget = QtWidgets.QWidget(MainWindow) 
          
        # pushbutton for loading data
        self.btn_loadData = QtWidgets.QPushButton(self.centralwidget)
        self.alignButton(self.btn_loadData,520, 10,APP_CONFIG.LOAD_DATA) 

        # pushbutton for analysing image
        self.btn_analyseData = QtWidgets.QPushButton(self.centralwidget)
        self.alignButton(self.btn_analyseData,520, 120,APP_CONFIG.PROCESS_IMAGE) 
        # pushbutton for saving image
        self.btn_saveData = QtWidgets.QPushButton(self.centralwidget)
        self.alignButton(self.btn_saveData,520, 230,APP_CONFIG.SAVE_DATA) 

        # add signals for the buttons  
        self.btn_loadData.clicked.connect(self.getImage) 
        self.btn_analyseData.clicked.connect(self.processImage)   
        self.btn_saveData.clicked.connect(self.saveImage)  

        # add label to hold and display the image
        self.label = QtWidgets.QLabel(self.centralwidget) 
        self.label.setGeometry(QtCore.QRect(APP_CONFIG.IMG_X,APP_CONFIG.IMG_Y, APP_CONFIG.IMG_WIDTH,APP_CONFIG.IMG_HEIGHT))       
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

        detVehicles_menu = QAction('Detect Vehicels', menubar) 
        detLanes_menu = QAction('Detect Lanes', menubar) 
        detectionAnalysis_menu = QAction('Analyse Detections', menubar) 

        docLink_menu    = QAction("Documentation",menubar)
        about_menu      = QAction("About",menubar)

        # register sub-menus with the main menu-bar     
        fileMenu.addAction(loadImage_menu)
        fileMenu.addAction(saveImage_menu)

        toolsMenu.addAction(detVehicles_menu)
        toolsMenu.addAction(detLanes_menu)
        toolsMenu.addAction(detectionAnalysis_menu)

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

    # This function acts as the slot for the button click signal
    # It opens up a window to select the image file that needs to be loaded into the application
    def getImage(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(MainWindow, 'Open file','c:\\', "Image files (*.jpg *.gif)")
        try:
            self.imagePath = fname[0]
            img = cv2.imread(self.imagePath)
            #resize image
            img = cv2.resize(img, self.img_resolution )
            self.image = img
            self.displayImageFromArray(img)
            self.displayStatus('Image loaded and ready for analysis.')
            return True
        except Exception as e:
            print(str(e))
            self.displayStatus('Error loading image.')
            return False

    def processImage(self):
        try:
            img = cv2.imread(self.imagePath)
            print("INFO: MAIN: Image read for analysis.")
            #pass the image to ImageAnalysis module to detect objects and draw bounding boxes
            print("INFO: MAIN: Processing image...")
            self.displayStatus('Starting image analysis...')
            procImg = ld.detectLanesWhite(img)
            procImg = cv2.resize(procImg, self.img_resolution )
            procImg = vd.detectVehicles(procImg)
            print("INFO: MAIN: Analysis done!")
            self.displayStatus('Image analysis finished.')
            procImg = cv2.resize(procImg, self.img_resolution )
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
            pixmap = QtGui.QPixmap(self.imagePath)
            height, width, channel = img.shape
            bytesPerLine = 3 * width
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
