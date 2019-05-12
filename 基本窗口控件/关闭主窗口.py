#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import QPushButton# 按钮
from PyQt5.QtWidgets import QHBoxLayout# 布局
from PyQt5.QtWidgets import QWidget
import sys

class MyWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setWindowTitle("关闭按钮")
        self.resize(800, 400)

        # 初始化按钮
        self.btn = QPushButton("关闭主窗口")
        self.btn.clicked.connect(self.onBtnClick)

        # 布局
        layout = QHBoxLayout()
        layout.addWidget(self.btn)

        main_frame = QWidget()
        main_frame.setLayout(layout)
        self.setCentralWidget(main_frame)

    def onBtnClick(self):
        # sender 是发送信号的对象
        sender = self.sender()
        print(sender.text() + '被按下了')
        qApp = QApplication.instance()
        qApp.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys(app.exec_())
