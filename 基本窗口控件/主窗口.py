#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # 窗口大小
        self.resize(800, 400)
        # 获取状态栏对象后，调用状态栏独享的shouwMessage（message, timeout）方法，显示状态栏
        self.status = self.statusBar()
        self.status.showMessage("这是状态栏提示", 5000)
        # title
        self.setWindowTitle("Pyqt5 maindow例子")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./images/cartoon1.ico'))
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())