#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit
from PyQt5.QtCore import Qt

class MyWidget(QWidget):

    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("行编辑")
        self.resize(800, 400)
        # 创建一个QLineEdit对象,设置默认
        lineEdit = QLineEdit("abbbb", self)
        # 设置对齐文本方式
        lineEdit.setAlignment(Qt.AlignCenter)
        # 设置文本的显示格式
        lineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        # 设置文本框是否可拖动
        lineEdit.setDragEnabled(True)
        # 全选
        lineEdit.selectAll()

        # 清除
        #lineEdit.clear()
        # 设置是否只读
        lineEdit.setReadOnly(True)
        # 设置是否可编辑
        lineEdit.setEnabled(True)
        # 获取文本
        connext = lineEdit.text()
        lineEdit.move(40, 40)
        # 如果输入框中的值有变化时，调用onChanged()方法
        lineEdit.textChanged[str].connect(self.onChanged)
        # 选择改变进行
        # lineEdit.selectionChanged[str].connect(self.selectionChanged)
        # 编辑文本结束
        lineEdit.editingFinished[True].connect(self.editingFinished)


    def onChanged(self, text):
        print("文本改变了" + text)

    # def selectionChanged(self, text):
    #     print("选择改变了" + text)

    def editingFinished(self, text):
        print("编辑完成" + text)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())