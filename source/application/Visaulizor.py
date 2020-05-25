from PyQt5 import QtCore, QtGui, QtWidgets
from pyexiv2 import Image
import os
def LoadMetadata(path):
        i= Image(path, encoding='utf-8')
        i.modify_exif({'Exif.Photo.MakerNote': 'test'})
        ex = i.read_exif()
        xm = i.read_xmp()
        Metadata = {**ex, **xm}    
        tableLength = len(Metadata)
        print (tableLength)
        del ex['Exif.Image.XPComment']
        return Metadata


def PopulateTable(Data):
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        for i, (k, v) in enumerate(Data.items()):
            # print(i, k, v)
            newitem1 = QtWidgets.QTableWidgetItem(k)
            newitem2 = QtWidgets.QTableWidgetItem(v)
            self.tableWidget.setItem(i, 0, newitem1)
            self.tableWidget.setItem(i, 1, newitem2)            


# def Visualize(self,path):
#     self.LoadMetadata(path)
#     self.generateTable()
#     self.PopulateTable(self.Metadata)        