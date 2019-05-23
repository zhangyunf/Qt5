#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei
import sys
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QRadioButton, QWidget
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyWidget(QWidget):

    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)
        self.btn1 = QRadioButton()
        self.btn2 = QRadioButton()
        self.create_UI()

    def create_UI(self):
        self.setWindowTitle("QRadioButton dome")
        # 初始化btn1
        self.btn1 = QRadioButton("button1")
        # 设置默认选中状态
        self.btn1.setCheckable(True)
        # 设置按钮选中状态发生变化时，发送信号
        self.btn1.toggled.connect(lambda: self.btnstate(self.btn1))

        # 初始化btn2
        self.btn2 = QRadioButton("button2")
        # 设置按钮选中状态发生变化时，发送信号
        self.btn2.toggled.connect(lambda: self.btnstate(self.btn2))

        # 布局
        layout = QHBoxLayout()
        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)
        self.setLayout(layout)

    def btnstate(self, btn):
        if btn.text() == "button1":
            if btn.isCheckable() == True:
                print(btn.text() + "is selected")
            else:
                print(btn.text() + "is deselected")

        if btn.text() == "button2":
            if btn.isCheckable() == True:
                print(btn.text() + "is selected")
            else:
                print(btn.text() + "is deselected")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())