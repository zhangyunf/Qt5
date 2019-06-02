#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Mywidget(QWidget):

    def __init__(self, parent=None):
        super(Mywidget, self).__init__(parent)
        self.setWindowTitle("QInputDialog dome")

        self.btn1 = QPushButton("获得列表里的选项")
        self.btn1.clicked.connect(self.getItem)
        self.le1 = QLineEdit()

        self.btn2 = QPushButton("获取字符串")
        self.btn2.clicked.connect(self.getText)
        self.le2 = QLineEdit()

        self.btn3 = QPushButton("获得整数")
        self.btn3.clicked.connect(self.getInt)
        self.le3 = QLineEdit()

        layout = QFormLayout()
        layout.addRow(self.btn1, self.le1)
        layout.addRow(self.btn2, self.le2)
        layout.addRow(self.btn3, self.le3)
        self.setLayout(layout)

    def getItem(self):
        items = ("C", "C++", "Java", "Python")
        item, ok = QInputDialog.getItem(self, "select input dialog", "语言列表", items, 0, False)
        if ok and item:
            self.le1.setText(item)

    def getText(self):
        text, ok = QInputDialog.getText(self, "text input dialog", "输入姓名")
        if ok:
            self.le2.setText(str(text))

    def getInt(self):
        num, ok = QInputDialog.getInt(self, "integer input dialog", "输入数字")
        if ok:
            self.le3.setText(str(num))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = Mywidget()
    widget.show()
    sys.exit(app.exec_())

