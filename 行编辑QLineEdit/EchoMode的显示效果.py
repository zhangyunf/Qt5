#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QFormLayout

class MyWidget(QWidget):

    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("EchoMode的显示效果")
        self.resize(800, 400)
        # 初始化QLineEdit
        pNormalLineEdit = QLineEdit()
        pNoEchoLineEdit = QLineEdit()
        pPasswordLineEdit = QLineEdit()
        pPasswordEchoOnEditLineEdit = QLineEdit()

        # 布局
        flo = QFormLayout()
        flo.addRow("Normal", pNormalLineEdit)
        flo.addRow("NoEcho", pNoEchoLineEdit)
        flo.addRow("password", pPasswordLineEdit)
        flo.addRow("passwordechoon", pPasswordEchoOnEditLineEdit)

        # 设置EchoMode
        pNormalLineEdit.setEchoMode(QLineEdit.Normal)
        pNoEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        pPasswordLineEdit.setEchoMode(QLineEdit.Password)
        pPasswordEchoOnEditLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        # 设置文本框浮现文字
        pNormalLineEdit.setPlaceholderText("Nomal")
        pNoEchoLineEdit.setPlaceholderText("NoEcho")
        pPasswordLineEdit.setPlaceholderText("password")
        pPasswordEchoOnEditLineEdit.setPlaceholderText("passwordEchoOn")

        # 添加布局
        self.setLayout(flo)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())