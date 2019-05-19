#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout, QLineEdit
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp

class MyWidget(QWidget):

    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("限制输入数字类型")
        self.resize(800, 400)
        # 初始化QLineEdit
        pInitQlineEdit = QLineEdit()
        pDoubleQLineEdit = QLineEdit()
        pValidatorQLineEdit = QLineEdit()

        # 布局
        flo = QFormLayout()
        flo.addRow("整数", pInitQlineEdit)
        flo.addRow("浮点数", pDoubleQLineEdit)
        flo.addRow("数字和字母", pValidatorQLineEdit)

        # 设置holder内容
        pInitQlineEdit.setPlaceholderText("整数")
        pDoubleQLineEdit.setPlaceholderText("浮点数")
        pValidatorQLineEdit.setPlaceholderText("字母和数字")

        # 构造整数验证器
        initVolidator = QIntValidator(self)
        initVolidator.setRange(100, 300)

        # 构造浮点数验证器
        doubleValidator = QDoubleValidator(self)
        doubleValidator.setRange(-10, 10)
        doubleValidator.setNotation(QDoubleValidator.StandardNotation)
        # 设置精度
        doubleValidator.setDecimals(2)

        # 构造数字字母验证器
        regExp = QRegExp("[a-zA-Z0-9]+$")
        regExpValidator = QRegExpValidator(self)
        regExpValidator.setRegExp(regExp)

        # 设置验证器
        pInitQlineEdit.setValidator(initVolidator)
        pDoubleQLineEdit.setValidator(doubleValidator)
        pValidatorQLineEdit.setValidator(regExpValidator)

        # 添加布局
        self.setLayout(flo)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())