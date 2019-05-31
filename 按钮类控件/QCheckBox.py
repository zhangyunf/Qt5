#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGroupBox, QCheckBox, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

class MyWidget(QWidget):

    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent)
        self.checkBox1 = None
        self.checkBox2 = None
        self.checkBox3 = None
        self.create_UI()

    def create_UI(self):
        self.setWindowTitle("QCheckBox dome")
        self.resize(800, 400)

        groupBox = QGroupBox("CheckBox")
        groupBox.setFlat(True)

        # 初始化checkbox1
        self.checkBox1 = QCheckBox("&&Checkbox1")
        # 设置选中复选框
        self.checkBox1.setChecked(True)
        # 当状态改变时发出的信号
        self.checkBox1.stateChanged.connect(lambda: self.btnstate(self.checkBox1))

        # 初始化checkbox2
        self.checkBox2 = QCheckBox("checkbox2")
        # 标记状态发生变化时，发出的信号
        self.checkBox2.toggled.connect(lambda: self.btnstate(self.checkBox2))

        # 初始化checkbox3
        self.checkBox3 = QCheckBox("checkbox3")
        # 设置复选框为一个三态复选框
        self.checkBox3.setTristate(True)
        # 设置
        self.checkBox3.setCheckState(Qt.PartiallyChecked)
        self.checkBox3.stateChanged.connect(lambda: self.btnstate(self.checkBox3))

        #布局
        layout = QHBoxLayout()
        layout.addWidget(self.checkBox1)
        layout.addWidget(self.checkBox2)
        layout.addWidget(self.checkBox3)

        groupBox.setLayout(layout)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(groupBox)

        self.setLayout(mainLayout)



    def btnstate(self, btn):
        chk1Status = self.checkBox1.text() + ', isChecked=' + str(self.checkBox1.isChecked()) + ', checkstatus=' + str(self.checkBox1.checkState()) + '\n'
        chk2Status = self.checkBox2.text() + ', isChecked=' + str(self.checkBox2.isChecked()) + ', checkstatus=' + str(self.checkBox2.checkState()) + '\n'
        chk3Status = self.checkBox3.text() + ', isChecked=' + str(self.checkBox3.isChecked()) + ', checkstatus=' + str(self.checkBox3.checkState()) + '\n'

        print(chk1Status + chk2Status + chk3Status)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())






