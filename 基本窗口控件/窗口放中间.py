#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei

from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
from PyQt5.QtWidgets import QDesktopWidget# 布局

class Winform(QMainWindow):

    def __init__(self, parent=None):

        super(Winform, self).__init__(parent)
        self.resize(800, 400)
        self.status = self.statusBar()
        self.status.showMessage("提示", 5000)
        self.setWindowTitle("窗口中间")
        self.center()

    def center(self):
        # 获取屏幕尺寸
        screen = QDesktopWidget().screenGeometry()
        # 获取软件当前尺寸
        size = self.geometry()
        # 移动到指定位置
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Winform()
    form.show()
    sys.exit(app.exec_())
