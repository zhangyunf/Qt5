#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei
import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
window = QWidget()
window.resize(800, 400)
window.move(250, 150)
window.setWindowTitle("第一个pyqt5应用")
window.show()
sys.exit(app.exec_())