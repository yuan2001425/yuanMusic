# -*- coding: utf-8 -*-
# @Time: 2023/12/25 下午1:48
# @Author: yuan425
# @Software: PyCharm

import sys

from PyQt5.QtWidgets import QApplication

from src.controller.controller import Controller
from src.model.model import Model
from src.view.view import View

if __name__ == '__main__':
    app = QApplication(sys.argv)
    model, view = Model(), View()
    controller = Controller(model, view)
    controller.show()
    sys.exit(app.exec_())
