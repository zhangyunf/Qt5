#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QFormLayout, QPushButton, QHBoxLayout
import sys

PATHLIST = ["网址：", "执行案例路径：", "JSON数据路径："]
class MyWidget(QWidget):
    is_editing = True
    is_run = True

    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent)
        self.__urlLineEdit = None
        self.__caseLineEdit = None
        self.__jsonLineEdit = None
        self.__runBtn = None
        self.__editBtn = None
        self.createUI()

    def createUI(self):
        self.setWindowTitle("自动化接口测试工具")
        self.resize(500, 200)
        # 初始化
        self.__urlLineEdit = QLineEdit()
        self.__caseLineEdit = QLineEdit()
        self.__jsonLineEdit = QLineEdit()
        # 增加布局
        flo = QFormLayout()
        flo.addRow(PATHLIST[0], self.__urlLineEdit)
        flo.addRow(PATHLIST[1], self.__caseLineEdit)
        flo.addRow(PATHLIST[2], self.__jsonLineEdit)
        flo.addRow(self.createBtn())

        # 增加编辑结束信号
        self.__urlLineEdit.editingFinished.connect(self.urlEditingFinished)
        self.__jsonLineEdit.editingFinished.connect(self.jsonEditingFinished)
        self.__caseLineEdit.editingFinished.connect(self.caseEditingFinshed)

        # 设置浮悬内容
        self.__urlLineEdit.setPlaceholderText("网址")
        self.__caseLineEdit.setPlaceholderText("存放案例路径")
        self.__jsonLineEdit.setPlaceholderText("存放json路径")

        # 禁止编辑
        self.endEdit()

        # 设置
        self.setLayout(flo)

    def createBtn(self):
        btnWidget = QWidget()
        # 初始化
        self.__runBtn = QPushButton("开始运行")
        self.__editBtn = QPushButton("编辑")

        # 创建一个水平布局
        hbox = QHBoxLayout()
        hbox.addWidget(self.__runBtn)
        hbox.addWidget(self.__editBtn)

        # 点击事件
        self.__runBtn.clicked.connect(self.runClick)
        self.__editBtn.clicked.connect(self.editClick)
        btnWidget.setLayout(hbox)
        return btnWidget

    def runClick(self):
        # 运行时，不允许修改
        if self.is_run:
            self.startRun()
        else:
            self.endRun()

    def startRun(self):
        self.is_run = False
        self.__runBtn.setText("运行中")
        self.__editBtn.setEnabled(False)
        self.endEdit()

    def endRun(self):
        self.is_run = True
        self.__runBtn.setText("开始运行")
        self.__editBtn.setEnabled(True)

    def editClick(self):
        # 修改时，不允许运行
        if self.is_editing:
            self.startEdit()
        else:
            self.endEdit()

    def startEdit(self):
        self.is_editing = False
        self.__runBtn.setEnabled(False)
        self.__editBtn.setText("保存")
        # 设置只读属性
        self.setLineEditEnabled(True)

    def endEdit(self):
        self.is_editing = True
        self.__runBtn.setEnabled(True)
        self.__editBtn.setText("编辑")
        # 设置只读属性
        self.setLineEditEnabled(False)

    def setLineEditEnabled(self, bool):
        self.__urlLineEdit.setEnabled(bool)
        self.__caseLineEdit.setEnabled(bool)
        self.__jsonLineEdit.setEnabled(bool)

    def urlEditingFinished(self):
        print("url编辑完成")

    def jsonEditingFinished(self):
        print("json编辑完成")

    def caseEditingFinshed(self):
        print("case编辑完成")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())