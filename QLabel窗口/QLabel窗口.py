#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei
'''
1、QLabel继承自QFrame
QObject---+
          |
        QPainDevice---+
                      |
                      QWindow---+
                                |
                                QFrame---+
                                         |
                                         QLabel

2、常用方法
setAlignment():按固定方式对齐文本
               Qt.AlignLeft，水平方向左对齐
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout
from PyQt5.QtCore import Qt# 布局
from PyQt5.QtGui import QPixmap, QPalette

class MyWidget(QWidget):

    def __init__(self):
        super(MyWidget, self).__init__()
        self.create_UI()

    def create_UI(self):
        self.setWindowTitle("QLabel")
        self.resize(800, 400)
        label1 = QLabel()
        label2 = QLabel()
        label3 = QLabel()
        label4 = QLabel()

        # 初始化标签控件
        label1.setText("第一个文本标签")# 添加文本
        label1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.blue)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href='#'>欢迎使用GUI</a>")

        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip("这是一个图片标签")
        label3.setPixmap(QPixmap('icon.jpg'))

        label4.setText("<a href='https://www.baidu.com'>链接</a>")
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip('超级链接')

        # 主窗口布局
        vbox = QHBoxLayout()
        vbox.addWidget(label1)
        vbox.addStretch()
        vbox.addWidget(label2)
        vbox.addStretch()
        vbox.addWidget(label3)
        vbox.addStretch()
        vbox.addWidget(label4)

        # 允许label1控件访问超链接
        label1.setOpenExternalLinks(True)
        # 打开循序访问超链接，默认是不允许，需要使用

        label4.setOpenExternalLinks(False)
        # 点击文本框绑定槽事件
        label4.linkActivated.connect( link_clicked )

        # 滑过文本框绑定槽事件
        label2.linkHovered.connect(link_hovered)
        label1.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.setLayout(vbox)

def link_clicked():
    print("label_4")

def link_hovered():
    print("label_2")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())