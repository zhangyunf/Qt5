#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei
import sys
from PyQt5.QtWidgets import QApplication,QWidget, QPushButton
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout# 布局模块

class MyWidget(QWidget):

    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent)
        self.createUI()

    def createUI(self):
        self.setWindowTitle("布局")
        self.resize(800, 400)

        # 绝对布局
        btn1 = QPushButton("绝对布局", self)
        btn1.move(20, 20)

        # 盒布局
        okBtn = QPushButton("ok")
        cancelBtn = QPushButton("cancel")

        hbox = QHBoxLayout()# 创建一个水平布局
        hbox.addStretch(1)# 增加弹性空间
        hbox.addWidget(okBtn)
        hbox.addWidget(cancelBtn)

        vbox = QVBoxLayout()# 垂直布局盒
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())
