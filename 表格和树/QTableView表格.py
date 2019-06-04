#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyWindow(QWidget):

    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setWindowTitle("QTableView dome")
        self.resize(500, 300)
        # 储存任意层次结构的数据
        self.model = QStandardItemModel(4, 4)
        self.model.setHorizontalHeaderLabels(["标题1", "标题2", "标题3", "标题4"])

        for row in range(4):
            for column in range(4):
                item = QStandardItem("row %s, column %s" % (row, column))
                self.model.setItem(row, column, item)

        self.tableView = QTableView()
        self.tableView.setModel(self.model)

        # 需要表格填满窗口
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 添加数据
        self.model.appendRow([QStandardItem("1"),
                              QStandardItem("2"),
                              QStandardItem("3")])

        hlaout = QHBoxLayout()
        self.btn = QPushButton("第一种删除")
        self.btn.clicked.connect(lambda: self.clicked(self.btn))
        self.btn1 = QPushButton("第二种删除")
        self.btn1.clicked.connect(lambda: self.clicked(self.btn1))
        hlaout.addWidget(self.btn)
        hlaout.addWidget(self.btn1)
        dlgLayput = QVBoxLayout()
        dlgLayput.addLayout(hlaout)
        dlgLayput.addWidget(self.tableView)
        self.setLayout(dlgLayput)

    def clicked(self, btn):
        if "第一" in btn.text():
            # 第一种删除
            indexs = self.tableView.selectionModel().selection().indexes()
            if len(indexs) > 0:
                # 取第一行的索引
                index = indexs[0]
                self.model.removeRows(index.row(), 1)
        else:
            index = self.tableView.currentIndex()
            print(index.row())
            self.model.removeRow(index.row())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    table = MyWindow()
    table.show()
    sys.exit(app.exec_())
