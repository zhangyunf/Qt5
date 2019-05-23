#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei
import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyWidget(QWidget):

    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent)
        self.btn1 = None
        self.btn2 = None
        self.btn3 = None
        self.btn4 = None
        self.create_UI()

    def create_UI(self):
        self.setWindowTitle("QPushButton dome")
        # 初始化
        self.btn1 = QPushButton("button1")
        # 设置选中状态--选中
        self.btn1.setCheckable(True)
        # 设置点击后的信号
        self.btn1.clicked.connect(lambda: self.whitchbtn(self.btn1))
        # 设置点击后的信号
        self.btn1.clicked.connect(self.btnstate)

        # 初始化btn2
        self.btn2 = QPushButton("Images")
        # 设置按钮图片
        self.btn2.setIcon(QIcon(QPixmap("./icon.jpg")))
        # 设置点击信号
        self.btn2.clicked.connect(lambda: self.whitchbtn(self.btn2))

        # 初始化btn3
        self.btn3 = QPushButton()
        # 设置不可编辑
        self.btn3.setEnabled(False)

        # 初始化btn4
        self.btn4 = QPushButton("&&D")
        # 设置按钮的默认状态
        self.btn4.setDefault(True)
        self.btn4.clicked.connect(lambda: self.whitchbtn(self.btn4))


        # 布局
        layout = QVBoxLayout()
        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)
        layout.addWidget(self.btn3)
        layout.addWidget(self.btn4)
        self.setLayout(layout)

    def whitchbtn(self, btn):
        print("clicked button is " + btn.text())

    def btnstate(self):
        if self.btn1.isChecked():
            print("pressed")
        else:
            print("released")




if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())