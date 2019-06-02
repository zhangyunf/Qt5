#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyWidget(QWidget):

    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent)
        self.setWindowTitle("QFontDialog dome")

        self.fontBtn = QPushButton("choose font")
        self.fontBtn.clicked.connect(self.choosefont)

        self.fontLabel = QLabel("hello,测试字体例子")

        layout = QVBoxLayout()
        layout.addWidget(self.fontLabel)
        layout.addWidget(self.fontBtn)
        self.setLayout(layout)


    def choosefont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.fontLabel.setFont(font)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())