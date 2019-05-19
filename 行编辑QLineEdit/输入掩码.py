#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei
import sys
from PyQt5.QtWidgets import QApplication, QFormLayout, QLineEdit, QWidget

class MyWidget(QWidget):

    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("掩码")

        # 初始化QLineEdit
        pIPQLineEdit = QLineEdit()
        pMACQLineEdit = QLineEdit()
        pDateQLineEdit = QLineEdit()
        pLicenseLineEdit = QLineEdit()

        # 布局
        flo = QFormLayout()
        flo.addRow("IP掩码", pIPQLineEdit)
        flo.addRow("MAC掩码", pMACQLineEdit)
        flo.addRow("Date掩码", pDateQLineEdit)
        flo.addRow("License掩码", pLicenseLineEdit)

        # 设置掩码
        pIPQLineEdit.setInputMask("000.000.000.000;_")
        pMACQLineEdit.setInputMask("HH:HH:HH:HH:HH:HH;_")
        pDateQLineEdit.setInputMask("0000-00-00")
        pLicenseLineEdit.setInputMask(">AAAA-AAAA-AAAA-AAAA-AAAA;#")

        self.setLayout(flo)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())