# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'two.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class UI(object):
    def __init__(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setMinimumSize(QtCore.QSize(720, 700))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(73, 96, 110))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 45, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 45, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 45, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 45, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 45, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 45, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 45, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 45, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(34, 45, 61))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QPushButton{\n"
"color:#ffffff;\n"
"font-size: 22px;\n"
"background-color: rgba(46, 204, 113, 0.4); \n"
"border-style: solid;\n"
"padding: 23px;\n"
"border-radius:10px\n"
"\n"
"}\n"
"QMainWindow{\n"
"background-color:#222d3d\n"
"}\n"
"\n"
"QWidget{\n"
"background-color:#222d3d\n"
"}\n"
"\n"
"QMenuBar{\\nbackground-color:#222d3d;\\n}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(719, 700))
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Image_GridLayout = QtWidgets.QGridLayout()
        self.Image_GridLayout.setObjectName("Image_GridLayout")
        self.loadImage = QtWidgets.QPushButton(self.centralwidget)
        self.loadImage.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loadImage.setStyleSheet("background-color: #ffb300; color:#000000; border: none;font-size:28px")
        self.loadImage.setObjectName("loadImage")
        self.Image_GridLayout.addWidget(self.loadImage, 1, 0, 1, 1)
        self.analyse = QtWidgets.QPushButton(self.centralwidget)
        self.analyse.setStyleSheet("background-color: #ffb300; color:#000000; border: none;font-size:28px")
        self.analyse.setObjectName("analyse")
        self.Image_GridLayout.addWidget(self.analyse, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("color:#ffb300; font-size:24px")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.Image_GridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.horizontalLayout.addLayout(self.Image_GridLayout)
        self.Analysis_gridLayout = QtWidgets.QGridLayout()
        self.Analysis_gridLayout.setObjectName("Analysis_gridLayout")
        self.Analysis_holder = QtWidgets.QListView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Analysis_holder.sizePolicy().hasHeightForWidth())
        self.Analysis_holder.setSizePolicy(sizePolicy)
        self.Analysis_holder.setStyleSheet("border-color: rgba(255, 255, 255, 0.5);\n"
"")
        self.Analysis_holder.setObjectName("Analysis_holder")
        self.Analysis_gridLayout.addWidget(self.Analysis_holder, 0, 0, 1, 2)
        self.report_generate = QtWidgets.QPushButton(self.centralwidget)
        self.report_generate.setEnabled(False)
        self.report_generate.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.report_generate.setStyleSheet("QPushButton{background-color: #ffb300; color:#000000; border: none;font-size:28px}\n"
"\n"
"QPushButton:disabled {\n"
"background-color:#989898;\n"
"}")
        self.report_generate.setObjectName("report_generate")
        self.Analysis_gridLayout.addWidget(self.report_generate, 2, 0, 1, 2)
        self.horizontalLayout.addLayout(self.Analysis_gridLayout)
        self.Table_verticalLayout = QtWidgets.QVBoxLayout()
        self.Table_verticalLayout.setObjectName("Table_verticalLayout")
        self.Metadata_table = QtWidgets.QTableWidget(self.centralwidget)
        self.Metadata_table.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Metadata_table.sizePolicy().hasHeightForWidth())
        self.Metadata_table.setSizePolicy(sizePolicy)
        self.Metadata_table.setStyleSheet("background-color: #29374b; color:#ffffff")
        self.Metadata_table.setShowGrid(False)
        self.Metadata_table.setGridStyle(QtCore.Qt.DotLine)
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
        self.Metadata_table.horizontalHeader().setVisible(False)
        self.Metadata_table.verticalHeader().setVisible(False)
        self.Table_verticalLayout.addWidget(self.Metadata_table)
        self.add_new = QtWidgets.QPushButton(self.centralwidget)
        self.add_new.setEnabled(False)
        self.add_new.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.add_new.setStyleSheet("QPushButton{background-color: #ffb300; color:#000000; border: none;font-size:28px}\n"
"\n"
"QPushButton:disabled {\n"
"background-color:#989898;\n"
"}")
        self.add_new.setObjectName("add_new")
        self.Table_verticalLayout.addWidget(self.add_new)
        self.horizontalLayout.addLayout(self.Table_verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 41))
        self.menubar.setStyleSheet("background-color: #1b2431; padding:10px; color:#ffffff")
        self.menubar.setObjectName("menubar")
        self.menuFIle = QtWidgets.QMenu(self.menubar)
        self.menuFIle.setObjectName("menuFIle")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFIle.menuAction())

        self.retranslateUi(MainWindow)
        self.add_new.clicked.connect(self.add_new.click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loadImage.setText(_translate("MainWindow", "Load Image"))
        self.analyse.setText(_translate("MainWindow", "Analyze "))
        self.label.setText(_translate("MainWindow", "Click on \"Load Image\" button to import an image"))
        self.report_generate.setText(_translate("MainWindow", "Generate Report"))
        item = self.Metadata_table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.Metadata_table.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.Metadata_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.Metadata_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Column"))
        self.add_new.setText(_translate("MainWindow", "Add new values to Metadata"))
        self.menuFIle.setTitle(_translate("MainWindow", "FIle"))


