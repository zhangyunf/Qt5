#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton, QVBoxLayout

class MyWidget(QWidget):

    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent)
        self.__textEdit = None
        self.__btnPress1 = None
        self.__btnPress2 = None
        self.initUI()


    def initUI(self):
        self.setWindowTitle("QTextEdit的使用")
        self.resize(800, 400)
        # 初始化
        self.__textEdit = QTextEdit()
        self.__btnPress1 = QPushButton("显示文本")
        self.__btnPress2 = QPushButton("显示HTML")

        # 布局
        layout = QVBoxLayout()
        layout.addWidget(self.__textEdit)
        layout.addWidget(self.__btnPress1)
        layout.addWidget(self.__btnPress2)

        # 添加按钮点击事件
        self.__btnPress1.clicked.connect(self.btn_press1_click)
        self.__btnPress2.clicked.connect(self.btn_press2_click)

        # QTextEdit内容改变时，发送信号
        self.__textEdit.textChanged.connect(self.textChanged)


        self.setLayout(layout)

    def btn_press1_click(self):
        # 清空内容
        self.__textEdit.clear()
        # 设置多行文本
        self.__textEdit.setPlainText("hello world \n 单机按钮")

    def btn_press2_click(self):
        # 清空内容
        self.__textEdit.clear()
        # 显示HTML文本
        self.__textEdit.setHtml("<font color='red' size='6'><red>hello pyqt5\n单机按钮</font>")

    def textChanged(self):
        print("内容改变" )

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())
