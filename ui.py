#!/usr/bin/env python
# -*- encoding: utf-8 -*-


from PyQt5.Qt import QProgressBar,QLabel
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5.QtCore import Qt
import time
from bili import down

class meun(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(268, 213)
        self.setWindowTitle("zRain")
        self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint,False)
        # self.setFixedSize(self.width(), self.height())
        self.setui()
        self.action()
    def setui(self):
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.label = QtWidgets.QLabel("AVID: ",self)
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.rad3 = QtWidgets.QRadioButton("普通视频",self)
        self.horizontalLayout_2.addWidget(self.rad3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.rad4 = QtWidgets.QRadioButton("番剧",self)
        self.horizontalLayout_2.addWidget(self.rad4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.qd = QtWidgets.QPushButton("确定",self)
        self.verticalLayout.addWidget(self.qd)
        self.qx = QtWidgets.QPushButton("取消",self)
        self.verticalLayout.addWidget(self.qx)
        self.progressBar = QtWidgets.QProgressBar(self)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.progressBar)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.rad1 = QtWidgets.QRadioButton("不进行转换(默认进行转换)",self)
        self.horizontalLayout_3.addWidget(self.rad1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.rad2 = QtWidgets.QRadioButton("转换后不删除源文件",self)
        self.horizontalLayout_3.addWidget(self.rad2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
    def action(self):
        self.rad3.setChecked(True)
        self.qd.clicked.connect(self.beg)
        self.qx.clicked.connect(lambda : self.close())
        self.rad3.clicked.connect(self.lablechange)
        self.rad4.clicked.connect(self.lablechange)
    def lablechange(self):
        if self.rad3.isChecked():
            self.label.setText("AVID: ")
        if self.rad4.isChecked():
            self.label.setText("EPID: ")
    def beg(self):
        if self.lineEdit.text()=="":
            return
        self.mit=down(self.lineEdit.text(),str(self.rad1.isChecked()),str(self.rad2.isChecked()),str(self.rad3.isChecked()))
        self.mit.data_.connect(self.bar_set)
        self.mit.start()
    def bar_set(self,value,stats):
        self.rad1.setEnabled(False)
        self.rad2.setEnabled(False)
        self.qd.setEnabled(False)
        all_stats=["下载flv视频文件%p%","下载mp4视频文件%p%","下载m4a音频文件%p%"]
        self.progressBar.setFormat(all_stats[stats])
        self.progressBar.setValue(value)
        if value==100:
            self.progressBar.reset()
            self.rad1.setEnabled(True)
            self.rad2.setEnabled(True)
            self.qd.setEnabled(True)


    
if __name__=='__main__':
    import sys
    app=QApplication(sys.argv)
    win=meun()
    win.show()
    sys.exit(app.exec_())
