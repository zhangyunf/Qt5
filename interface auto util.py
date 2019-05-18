#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei
from PyQt5.QtWidgets import QLabel, QWidget, QApplication, QLineEdit, QGridLayout
import sys

PATHLIST = ["网址：", "执行案例路径：", "JSON数据路径："]
class MyWidget(QWidget):

    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent)
        self.createUI()

    def createUI(self):
        self.setWindowTitle("自动化接口测试工具")
        self.resize(800, 400)

        url_label = QLabel(PATHLIST[0])
        url_edit = QLineEdit()

        case_label = QLabel(PATHLIST[1])
        case_edit = QLineEdit()

        json_label = QLabel(PATHLIST[2])
        json_edit  = QLineEdit()

        grid = QGridLayout()
        grid.setSpacing(1)

        grid.addWidget(url_label, 1, 0)
        grid.addWidget(url_edit, 1, 1)
        grid.addWidget(case_label, 2, 0)
        grid.addWidget(case_edit, 2, 1)
        grid.addWidget(json_label, 3, 0)
        grid.addWidget(json_edit, 3, 1)
        self.setLayout(grid)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())