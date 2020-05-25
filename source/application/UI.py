from PyQt5 import QtCore, QtGui, QtWidgets

class UI(object):
    def __init__(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setMinimumSize(QtCore.QSize(720, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(719, 700))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)

        self.gridLayout.setObjectName("gridLayout")
        self.Image_GridLayout = QtWidgets.QGridLayout()
        self.Image_GridLayout.setObjectName("Image_GridLayout")
        
        # self.ImageHolder = QtWidgets.QFrame(self.centralwidget)
        # self.ImageHolder.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.ImageHolder.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.ImageHolder.setObjectName("ImageHolder")
        # self.Image_GridLayout.addWidget(self.ImageHolder, 0, 0, 1, 2)
        # self.ImageHolder = QtWidgets.QLabel(self.centralwidget)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.ImageHolder.sizePolicy().hasHeightForWidth())
        # self.ImageHolder.setSizePolicy(sizePolicy)
        # self.ImageHolder.setObjectName("ImageHolder")
        # self.Image_GridLayout.addWidget(self.ImageHolder, 0, 0, 1, 2)
      
        
        self.label = QtWidgets.QLabel(self.centralwidget) 
        self.label.setText("Select an Image.")  
        self.label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Image_GridLayout.addWidget(self.label, 0, 0, 1, 2)

        #buttons
        self.loadImage = QtWidgets.QPushButton(self.centralwidget)
        self.loadImage.setObjectName("loadImage")
        
        self.Image_GridLayout.addWidget(self.loadImage, 1, 0, 1, 1)
        self.analyse = QtWidgets.QPushButton(self.centralwidget)
        self.analyse.setObjectName("analyse")
        self.Image_GridLayout.addWidget(self.analyse, 1, 1, 1, 1)
        
        self.gridLayout.addLayout(self.Image_GridLayout, 0, 0, 1, 1)
        #metadata container
        self.Table_verticalLayout = QtWidgets.QVBoxLayout()
        self.Table_verticalLayout.setObjectName("Table_verticalLayout")
        self.Metadata_table = QtWidgets.QTableWidget(self.centralwidget)
        self.Metadata_table.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Metadata_table.sizePolicy().hasHeightForWidth())
        self.Metadata_table.setSizePolicy(sizePolicy)
        self.Metadata_table.setObjectName("Metadata_table")
        self.Metadata_table.setColumnCount(2)
        self.Metadata_table.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.Metadata_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Metadata_table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Metadata_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Metadata_table.setHorizontalHeaderItem(1, item)
        self.Table_verticalLayout.addWidget(self.Metadata_table)
        self.add_new = QtWidgets.QPushButton(self.centralwidget)
        self.add_new.setObjectName("add_new")
        self.Table_verticalLayout.addWidget(self.add_new)
        #analysis container
        self.gridLayout.addLayout(self.Table_verticalLayout, 0, 2, 1, 1)
        self.Analysis_horizontalLayout = QtWidgets.QHBoxLayout()
        self.Analysis_horizontalLayout.setObjectName("Analysis_horizontalLayout")
        self.analysis_listview = QtWidgets.QListView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.analysis_listview.sizePolicy().hasHeightForWidth())
        self.analysis_listview.setSizePolicy(sizePolicy)
        self.analysis_listview.setObjectName("analysis_listview")
        self.Analysis_horizontalLayout.addWidget(self.analysis_listview)
        self.gridLayout.addLayout(self.Analysis_horizontalLayout, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 38))
        self.menubar.setObjectName("menubar")
        self.menuFIle = QtWidgets.QMenu(self.menubar)
        self.menuFIle.setObjectName("menuFIle")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFIle.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loadImage.setText(_translate("MainWindow", "Load Image"))
        self.analyse.setText(_translate("MainWindow", "Analyse"))
        item = self.Metadata_table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.Metadata_table.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.Metadata_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.Metadata_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Column"))
        self.add_new.setText(_translate("MainWindow", "PushButton"))
        self.menuFIle.setTitle(_translate("MainWindow", "FIle"))
