#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Mywidget(QWidget):

    def __init__(self, parent=None):
        super(Mywidget, self).__init__(parent)
        self.setWindowTitle("QMessageBox dome")
        self.resize(300, 100)

        self.btn = QPushButton("点击弹出消息盒子", self)
        self.btn.clicked.connect(self.clicked)
        reply = QMessageBox.information(self, "标题", "消息正文", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    def clicked(self):
        # 使用information
        reply = QMessageBox.information(self, "标题", "消息正文", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        print(reply)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = Mywidget()
    widget.show()
    sys.exit(app.exec_())