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
        self.sl = None
        self.create_UI()

    def create_UI(self):
        self.setWindowTitle("QSlider dome")
        self.resize(300, 100)

        self.l1 = QLabel('hello pyqt5')
        self.l1.setAlignment(Qt.AlignCenter)

        self.sl = QSlider(Qt.Horizontal)
        # 设置最小值
        self.sl.setMinimum(10)
        # 设置最大值
        self.sl.setMaximum(100)
        # 步长
        self.sl.setSingleStep(1)
        # 设置当前值s
        self.sl.setValue(20)
        # 设置刻度位置，下方
        self.sl.setTickPosition(QSlider.TicksBelow)
        # 设置刻度间隔
        self.sl.setTickInterval(5)
        # 当值发生改变时发出的信号
        self.sl.valueChanged.connect(self.valuechange)

        # 布局
        layout = QVBoxLayout()
        layout.addWidget(self.l1)
        layout.addWidget(self.sl)
        self.setLayout(layout)

    def valuechange(self):
        print('current slider value=%s' % self.sl.value())
        size = self.sl.value()
        self.l1.setFont(QFont("Arial", size))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWiget()
    widget.show()
    sys.exit(app.exec_())