#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class MyWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle("Icon")
        # windows 中设置左上角图标
        self.setWindowIcon(QIcon("icon.jpg"))
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 设置程序图标
    app.setWindowIcon(QIcon("icon.jpg"))
    ex = MyWidget()
    sys.exit(app.exec_())