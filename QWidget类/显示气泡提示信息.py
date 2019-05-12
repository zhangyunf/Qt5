#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIcon
class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):

        QToolTip.setFont(QFont("SansSerif", 10))
        self.setToolTip("提示")
        self.setWindowTitle("显示气泡提示信息")
        self.setGeometry(200, 300, 400, 400)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.jpg"))
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())