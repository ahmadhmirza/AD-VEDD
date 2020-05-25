from PyQt5 import QtCore, QtGui, QtWidgets 

import sys 
import cv2
import Config as APP_CONFIG
import Visaulizor as vs
# import VehicleDetection as vd
# import LaneDetection as ld
from PyQt5.QtGui import QImage

class Ui_MainWindow(object): 
    def __init__(self):
        super().__init__()
        self.title          =   APP_CONFIG.MAIN_WINDOW_TITLE
        self.left           =   APP_CONFIG.LEFT
        self.top            =   APP_CONFIG.TOP
        self.width          =   APP_CONFIG.WIDTH
        self.height         =   APP_CONFIG.HEIGHT
        self.img_resolution = (APP_CONFIG.WIDTH, APP_CONFIG.HEIGHT)
        self.TableLength = 10
    def getImage(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(MainWindow, 'Open file','E:\\', "Image files (*.jpg *.gif)")
        try:
            self.imagePath = fname[0]
            img = cv2.imread(self.imagePath)
            #resize image
            img = cv2.resize(img, self.img_resolution )
            self.displayImageFromArray(img)
            self.Metadata = vs.LoadMetadata(self.imagePath)
            self.TableLength = len(self.Metadata)
            # self.generateTable(self.TableLength) 
            for i, (k, v) in enumerate(self.Metadata.items()):
                # print(i, k, v)
                newitem1 = QtWidgets.QTableWidgetItem(k)
                newitem2 = QtWidgets.QTableWidgetItem(v)
                self.tableWidget.setItem(i, 0, newitem1)
                self.tableWidget.setItem(i, 1, newitem2)     

            return True
        except Exception as e:
            print(str(e))
            return False

    def setupUi(self, MainWindow): 
        MainWindow.setWindowTitle(self.title)
        MainWindow.setGeometry(self.left, self.top, self.width, self.height)
        #Fix window size so maximizing does not distort the layout.
        # MainWindow.setFixedSize(self.width, self.height)
        self.centralwidget = QtWidgets.QWidget(MainWindow) 
          
        # pushbutton for loading data
        self.btn_loadData = QtWidgets.QPushButton(self.centralwidget)
        self.alignButton(self.btn_loadData,520, 10,APP_CONFIG.LOAD_DATA) 

        # pushbutton for analysing image
        self.btn_analyseData = QtWidgets.QPushButton(self.centralwidget)
        self.alignButton(self.btn_analyseData,520, 120,APP_CONFIG.PROCESS_IMAGE) 

        # #show metadata
        # self.btn_verboseData = QtWidgets.QPushButton(self.centralwidget)
        # self.alignButton(self.btn_verboseData,520, 250,APP_CONFIG.SHOW_DATA) 
        
        # add signals for the buttons  
        self.btn_loadData.clicked.connect(self.getImage) 
        # self.btn_verboseData.clicked.connect(self.generateTable) 

        # self.btn_analyseData.clicked.connect(self.processImage)    
        # add label to hold and display the image
        self.label = QtWidgets.QLabel(self.centralwidget) 
        self.label.setGeometry(QtCore.QRect(APP_CONFIG.IMG_X,APP_CONFIG.IMG_Y, APP_CONFIG.IMG_WIDTH,APP_CONFIG.IMG_HEIGHT))       
        # The set for the label is set to empty for now.
        self.label.setText("Select an Image.")  
        self.label.setFrameShape(QtWidgets.QFrame.Panel)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.generateTable(self.TableLength)
        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow) 
  
    def alignButton(self,qtPushButton,x,y,caption):
        qtPushButton.setGeometry(QtCore.QRect(x, y, APP_CONFIG.BTN_WIDTH, APP_CONFIG.BTN_HEIGHT)) 
        qtPushButton.setText(caption)
        return True
    def generateTable(self,TableLength):    
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(1000, 10, 571, 601))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(self.TableLength)
        print(self.TableLength)
    # This function aligns the UI to the center of the screen
    def centerWindow(self):
        qtRectangle = self.frameGeometry()
        print(str(qtRectangle))
        centerPoint = QDesktopWidget().availableGeometry().center() 
        qtRectangle.moveCenter(centerPoint)
        MainWindow.move(qtRectangle.topLeft())
        return True

    # This function acts as the slot for the button click signal
    # It opens up a window to select the image file that needs to be loaded into the application
    # def processImage(self):
    #     try:
    #         img = cv2.imread(self.imagePath)
    #         print("INFO: MAIN: Image read for analysis.")
    #         #pass the image to ImageAnalysis module to detect objects and draw bounding boxes
    #         print("INFO: MAIN: Processing image...")
    #         procImg = ld.detectLanesWhite(img)
    #         procImg = cv2.resize(procImg, self.img_resolution )
    #         procImg = vd.detectVehicles(procImg)
    #         print("INFO: MAIN: Analysis done!")
    #         procImg = cv2.resize(procImg, self.img_resolution )
    #         self.displayImageFromArray(procImg)
    #         print("INFO: MAIN: Process finished.")
    #         return True
    #     except Exception as e:
    #         print("ERROR: MAIN:" + str(e))
    #         return False


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
