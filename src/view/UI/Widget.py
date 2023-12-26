# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(590, 620)
        Widget.setMinimumSize(QtCore.QSize(590, 620))
        Widget.setMaximumSize(QtCore.QSize(590, 620))
        self.label = QtWidgets.QLabel(Widget)
        self.label.setGeometry(QtCore.QRect(20, 20, 80, 30))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(Widget)
        self.groupBox.setGeometry(QtCore.QRect(20, 60, 550, 460))
        self.groupBox.setObjectName("groupBox")
        self.listWidget = QtWidgets.QListWidget(self.groupBox)
        self.listWidget.setGeometry(QtCore.QRect(10, 30, 530, 420))
        self.listWidget.setObjectName("listWidget")
        self.lineEdit = QtWidgets.QLineEdit(Widget)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QtCore.QRect(110, 20, 400, 30))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_path = QtWidgets.QPushButton(Widget)
        self.pushButton_path.setGeometry(QtCore.QRect(520, 20, 51, 31))
        self.pushButton_path.setObjectName("pushButton_path")
        self.horizontalSlider = QtWidgets.QSlider(Widget)
        self.horizontalSlider.setEnabled(False)
        self.horizontalSlider.setGeometry(QtCore.QRect(20, 530, 440, 20))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label_progress = QtWidgets.QLabel(Widget)
        self.label_progress.setGeometry(QtCore.QRect(480, 530, 90, 20))
        self.label_progress.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_progress.setObjectName("label_progress")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 560, 551, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox_mode = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_mode.setObjectName("comboBox_mode")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.comboBox_mode.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_mode)
        self.pushButton_pre = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_pre.setEnabled(False)
        self.pushButton_pre.setObjectName("pushButton_pre")
        self.horizontalLayout.addWidget(self.pushButton_pre)
        self.pushButton_play = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_play.setEnabled(False)
        self.pushButton_play.setObjectName("pushButton_play")
        self.horizontalLayout.addWidget(self.pushButton_play)
        self.pushButton_next = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_next.setEnabled(False)
        self.pushButton_next.setObjectName("pushButton_next")
        self.horizontalLayout.addWidget(self.pushButton_next)
        self.comboBox_speed = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_speed.setObjectName("comboBox_speed")
        self.comboBox_speed.addItem("")
        self.comboBox_speed.addItem("")
        self.comboBox_speed.addItem("")
        self.comboBox_speed.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_speed)

        self.retranslateUi(Widget)
        self.comboBox_speed.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "远哥挺乐-音乐播放器"))
        self.label.setText(_translate("Widget", "歌单目录："))
        self.groupBox.setTitle(_translate("Widget", "播放列表"))
        self.pushButton_path.setText(_translate("Widget", "打开"))
        self.label_progress.setText(_translate("Widget", "00:00/00:00"))
        self.comboBox_mode.setItemText(0, _translate("Widget", "列表循环"))
        self.comboBox_mode.setItemText(1, _translate("Widget", "单曲循环"))
        self.comboBox_mode.setItemText(2, _translate("Widget", "随机播放"))
        self.pushButton_pre.setText(_translate("Widget", "上一曲"))
        self.pushButton_play.setText(_translate("Widget", "播放"))
        self.pushButton_next.setText(_translate("Widget", "下一曲"))
        self.comboBox_speed.setItemText(0, _translate("Widget", "0.5x"))
        self.comboBox_speed.setItemText(1, _translate("Widget", "1.0x"))
        self.comboBox_speed.setItemText(2, _translate("Widget", "1.5x"))
        self.comboBox_speed.setItemText(3, _translate("Widget", "2.0x"))
