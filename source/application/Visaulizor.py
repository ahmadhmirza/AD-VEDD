from PyQt5 import QtCore, QtGui, QtWidgets
from pyexiv2 import Image
from UI import *
import os
import re
class Visualisor(UI):
        def getImagePath(self, path):
                self.path = path
                return(self.path)
        def LoadMetadata(self, path):
                i= Image(path, encoding='utf-8')
                i.modify_exif({'Exif.Photo.MakerNote': 'test'})
                ex = i.read_exif()
                print(len(ex))
                xm = i.read_xmp()
                self.Metadata = {**ex, **xm}    
                self.tableLength = len(self.Metadata)
                print (self.tableLength)
                del ex['Exif.Image.XPComment']
                self.Metadata_table.setRowCount(self.tableLength)
                # self.PopulateTable(self.Metadata)
                self.p = 'Exif.'
                for i, (k, v) in enumerate(self.Metadata.items()):
                        k= re.sub('Exif.','',k)  
                        k= re.sub('Xmp.','',k)                              
                        print(i, k, v)
                        self.newitem1 = QtWidgets.QTableWidgetItem(k)
                        self.newitem2 = QtWidgets.QTableWidgetItem(v)
                        self.Metadata_table.setItem(i, 0, self.newitem1)
                        self.Metadata_table.setItem(i, 1, self.newitem2)   
                return self.Metadata
