#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyWiget(QWidget):

    def __init__(self, parent=None):
        super(MyWiget, self).__init__(parent)
        self.l1 = None
        self.sp = None
        self.create_UI()

    def create_UI(self):
        self.setWindowTitle("QSpinBox dome")
        self.resize(300, 100)

        self.l1 = QLabel('current value:')
        self.l1.setAlignment(Qt.AlignCenter)

        self.sp = QSpinBox()
        # 设置最大值、最小值、步长
        self.sp.setRange(0, 10)
        # 值改变时发出的信号
        self.sp.valueChanged.connect(self.valuechang)

        layout = QVBoxLayout()
        layout.addWidget(self.l1)
        layout.addWidget(self.sp)
        self.setLayout(layout)

    def valuechang(self):
        self.l1.setText("current vlaue:" + str(self.sp.value()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWiget()
    widget.show()
    sys.exit(app.exec_())