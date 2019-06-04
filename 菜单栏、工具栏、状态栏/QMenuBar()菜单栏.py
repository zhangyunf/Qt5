#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyWidget(QMainWindow):

    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent)
        layout = QHBoxLayout()
        self.setWindowTitle("menu 例子")

        # 返回主窗口QMenuBar对象
        bar = self.menuBar()
        # 在菜单栏中添加一个新的QMenu对象
        file = bar.addMenu("File")
        # 向QMenu小控件中添加一个操作按钮，其中包含文本或图标
        file.addAction("New")

        save = QAction("Save", self)
        save.setShortcut("Ctrl+S")
        file.addAction(save)

        edit = file.addMenu("Edit")
        edit.addAction("copy")
        edit.addAction("paste")

        quit = QAction("Quit", self)
        file.addAction(quit)

        file.triggered[QAction].connect(self.processtrigger)


        self.setLayout(layout)

    def processtrigger(self, q):
        print(q.text() + 'is triggered')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())



