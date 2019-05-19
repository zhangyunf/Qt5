#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei
import sys
from PyQt5.QtWidgets import QApplication, QFormLayout, QWidget, QLineEdit
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator, QFont
from PyQt5.QtCore import Qt

class MyWidget(QWidget):

    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent)
        self.creatUI()

    def creatUI(self):
        self.setWindowTitle("综合示例")
        # 初始化
        el = QLineEdit()
        # 设置验证器
        el.setValidator(QIntValidator())
        # 设置允许输入最大长度
        el.setMaxLength(4)
        #  设置文本对齐类型
        el.setAlignment(Qt.AlignCenter)
        # 设置字体
        el.setFont(QFont("Arial", 20))

        e2 = QLineEdit()
        # 设置验证器
        e2.setValidator(QDoubleValidator(0.99, 99.99, 2))
        flo = QFormLayout()
        flo.addRow("integer validator", el)
        flo.addRow("double validator", e2)

        e3 = QLineEdit()
        # 设置掩码
        e3.setInputMask("+99_9999_99999")
        flo.addRow("input mask", e3)

        e4 = QLineEdit()
        # 设置浮悬显示内容
        e4.setPlaceholderText("浮悬")
        # 内容改变时，发送信号
        e4.textChanged.connect(self.textChanged)

        e5 = QLineEdit()
        # 设置EchoMode显示
        e5.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        flo.addRow("password", e5)

        e6 = QLineEdit("hello world")
        # 设置只读
        e6.setReadOnly(True)
        flo.addRow("只读", e6)

        e7 = QLineEdit()
        # 完成编辑时的信号
        e7.editingFinished.connect(self.editingFinished)
        flo.addRow("编辑完成", e7)

        self.setLayout(flo)

    def textChanged(self, text):
        print("改变")

    def editingFinished(self):
        print("编辑完成")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())
