#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyWidget(QWidget):

    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent)
        self.setWindowTitle("QFileDialog dome")

        self.btn = QPushButton("加载图片")
        self.btn.clicked.connect(self.getfile)

        self.le = QLabel("")

        self.btn1 = QPushButton("加载文件")
        self.btn1.clicked.connect(self.getfiles)

        self.contents = QTextEdit()

        layout = QVBoxLayout()
        layout.addWidget(self.btn)
        layout.addWidget(self.le)
        layout.addWidget(self.btn1)
        layout.addWidget(self.contents)

        self.setLayout(layout)

    def getfile(self):
        fname, _ = QFileDialog.getOpenFileName(self, "open file", "c:\\", "Image files (*.jpg *.gif)")
        self.le.setPixmap(QPixmap(fname))

    def getfiles(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setFilter(QDir.Files)
        if dlg.exec_():
            filenames = dlg.selectedFiles()
            f = open(filenames[0], 'r')

            with f:
                data = f.read()
                self.contents.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())