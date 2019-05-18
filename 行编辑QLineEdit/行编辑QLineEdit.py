#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit

class MyWidget(QWidget):

    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("行编辑")
        self.resize(800, 400)
        # 创建一个QLineEdit对象,设置默认
        lineEdit = QLineEdit("abbbb", self)
        # 清除
        lineEdit.clear()
        # 设置是否可编辑
        lineEdit.setReadOnly(True)
        # 获取文本
        connext = lineEdit.text()
        lineEdit.move(40, 40)
        # 如果输入框中的值有变化时，调用onChanged()方法
        lineEdit.textChanged[str].connect(self.onChanged)

    def onChanged(self, text):
        print(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())