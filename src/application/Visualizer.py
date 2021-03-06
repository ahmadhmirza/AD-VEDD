from PyQt5 import QtCore, QtGui, QtWidgets
from pyexiv2 import Image
from UI_Layout import *
from UI_Dialog import *
import os
import re

class Visualisor(UI,Ui_Dialog):
        
        def LoadMetadata(self, path):
                self.path = path
                try:
                        i= Image(path, encoding='utf-8')
                        # i.modify_exif({'Exif.Photo.MakerNote': ''})
                        ex = i.read_exif()
                        print("Metadata entries found:" + str(len(ex)))
                        xm = i.read_xmp()
                        self.Metadata = {**ex, **xm}    
                        self.tableLength = len(self.Metadata)
                        print (self.tableLength)
                        # del ex['Exif.Image.XPComment']
                        self.Metadata_table.setRowCount(self.tableLength)
                        
                        # self.PopulateTable(self.Metadata)
                        self.p = 'Exif.'
                        for i, (k, v) in enumerate(self.Metadata.items()):
                                k= re.sub('Exif.','',k)  
                                k= re.sub('Xmp.','',k)                              
                                # print(i, k, v)
                                self.newitem1 = QtWidgets.QTableWidgetItem(k)
                                self.newitem2 = QtWidgets.QTableWidgetItem(v)
                                self.Metadata_table.setItem(i, 0, self.newitem1)
                                self.Metadata_table.setItem(i, 1, self.newitem2)
                        header = self.Metadata_table.horizontalHeader()
                        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
                        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
                        return True
                except Exception as e:
                        print("visualizer: " + str(e))

                        self.Metadata_table.setRowCount(1)
                        self.Metadata_table.setColumnCount(2)
                        self.Metadata_table.setItem(1,1, QtWidgets.QTableWidgetItem("ERROR"))
                        self.Metadata_table.setItem(1,1, QtWidgets.QTableWidgetItem(str(e)))
                        return str(e)
        def one(self):
                if self.Metadata_table:
                        self.add_new.setEnabled(True)


