#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyWidget(QWidget):

    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent)
        self.lbl = None
        self.cb = None
        self.create_UI()

    def create_UI(self):
        self.setWindowTitle("QComboBox dome")
        self.resize(300, 90)

        self.lbl = QLabel("")
        self.cb = QComboBox()
        # 添加下拉选项
        self.cb.addItem("C")
        self.cb.addItem("C++")
        # 添加多个下拉选项
        self.cb.addItems(["Java", "C#", "Python"])
        # 选中项改变时发出的信号
        self.cb.currentIndexChanged.connect(self.selectionchange)

        # 布局
        layout = QVBoxLayout()
        layout.addWidget(self.lbl)
        layout.addWidget(self.cb)
        self.setLayout(layout)

    def selectionchange(self, i):
        #显示选中项
        self.lbl.setText(self.cb.currentText())
        print("Items in the list are:")
        # 获取选项总数
        for count in range(self.cb.count()):
            # 获取指定位置的选项信息
            print("item" + str(count) + "=" + self.cb.itemText(count))
            print('current index', i, 'selection changed', self.cb.currentText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())