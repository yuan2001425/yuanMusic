# -*- coding: utf-8 -*-
# @Time: 2023/12/25 下午2:43
# @Author: yuan425
# @Software: PyCharm

import os
import random

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QFileDialog, QMessageBox

ALLOW_VOICE_TYPE = [".mp3", ".wav"]  # 允许读取的音频文件类型


# 秒转时间格式
def seconds_to_time(s):
    minutes = int(s // 60)
    seconds = int(s % 60)
    return f"{minutes:02d}:{seconds:02d}"


class Controller(QDialog):
    def __init__(self, model, view):
        super(Controller, self).__init__()
        # 加载模型
        self._model = model
        # 加载渲染
        self._view = view
        self._view.setupUi(self)
        # 弹出框初始化
        self.msg_box = QMessageBox()
        self.msg_box.setWindowTitle("通知")
        # 文件夹选择框初始化
        self.file_dialog = QFileDialog()
        self.file_dialog.setDirectory(self._model.music_base_path)

        # 绑定事件
        self._view.pushButton_path.clicked.connect(self.click_on_choose_path)
        self._view.horizontalSlider.valueChanged.connect(self.slider_value_changed)
        self._view.horizontalSlider.sliderPressed.connect(self.music_pause)
        self._view.horizontalSlider.sliderReleased.connect(self.music_start)
        self._view.pushButton_play.clicked.connect(self.click_on_play_button)
        self._view.pushButton_pre.clicked.connect(lambda: self.update_pre_play(next_music_idx=-2))
        self._view.pushButton_next.clicked.connect(lambda: self.update_pre_play(next_music_idx=-1))
        self._view.listWidget.itemDoubleClicked.connect(self.list_item_clicked)
        self._view.comboBox_speed.currentIndexChanged.connect(self.speed_changed)

        self._model.data_signal.connect(self.update_view)

    def click_on_choose_path(self):
        folder_path = self.file_dialog.getExistingDirectory(self, "选择文件夹")
        if folder_path:
            file_list = []
            file_type_dict = {}  # 用来计数的字典
            # 遍历文件夹中的所有文件
            for file in os.listdir(folder_path):
                # 检查文件扩展名是否处于 ALLOW_VOICE_TYPE 中
                for check in ALLOW_VOICE_TYPE:
                    if file.lower().endswith(check):
                        file_type_dict[check] = file_type_dict.get(check, 0) + 1
                        file_list.append(file)
            if sum(value for key, value in file_type_dict.items()) > 0:  # 存在有效音频文件
                self._model.music_base_path = folder_path  # 更改歌单目录地址
                self._model.music_list = file_list  # 更改歌曲列表
                self.update_view({  # 更新页面信息
                    "music_base_path": self._model.music_base_path,
                    "music_list": self._model.music_list,
                    "information": {
                        "code": 0,
                        "message": "找到有效文件：\n" + "\n".join(
                            f"{key}: {value}" for key, value in file_type_dict.items())
                    }
                })
                self._model.initial_music()  # 获取当前音乐并加载
            else:  # 不存在有效音频文件
                self.update_view({  # 更新页面信息
                    "information": {
                        "code": 1,
                        "message": "没有有效文件"
                    }
                })

    def play(self):
        # 列表高亮
        if self._model.pre_play[0] < 0:  # 上一曲index
            self._model.pre_play[0] = len(self._model.music_list) - 1
        self._view.listWidget.item(self._model.pre_play[0]).setSelected(False)
        item = self._model.pre_play[1]  # 当前歌曲index
        self._view.listWidget.item(item).setSelected(True)
        # 初始化时长显示
        start_second = 0
        total_second = self._model.player.total_second
        self._view.label_progress.setText(seconds_to_time(start_second) + '/' + seconds_to_time(total_second))
        # 初始化进度条
        self._view.horizontalSlider.setMaximum(int(total_second))  # 设置最大值
        self._view.horizontalSlider.setValue(int(start_second))  # 设置当前值
        # 解锁按钮
        self.change_buttons_state(target_state=True)
        # 自动开始播放音乐
        self.music_start()

    def list_item_clicked(self, item):
        idx = self._model.music_list.index(item.text())
        if idx != self._model.pre_play[1]:  # 反复点击的不算
            self.update_pre_play(next_music_idx=idx)

    def speed_changed(self):
        # 当前播放速度
        speed = eval(self._view.comboBox_speed.currentText()[:-1])
        # 修改文件播放速度
        self._model.player.speed = speed
        self._model.player.change_speed()
        # 修改定时器刷新时间
        self._model.timer.setInterval(int(1000 / speed))

    def update_pre_play(self, next_music_idx=-1):
        # 下一首歌曲，默认-1即根据播放顺序来
        if next_music_idx != -1:
            if next_music_idx == -2:  # 上一首，和当前首调换
                self._model.pre_play.reverse()
            else:  # 根据列表选择
                self._model.pre_play = [self._model.pre_play[1], next_music_idx]
        else:
            mode_idx = self._view.comboBox_mode.currentIndex()  # 列表/单曲/随机
            if mode_idx == 0:
                self._model.pre_play = [(x + 1) % len(self._model.music_list) for x in self._model.pre_play]
            elif mode_idx == 1:
                pass
            elif mode_idx == 2:
                self._model.pre_play = [self._model.pre_play[1], random.randint(0, len(self._model.music_list) - 1)]
        self.music_pause()  # 停止当前音乐
        self._model.initial_music()  # 获取新的音乐并加载
        self.play()  # 执行新的音乐播放流程

    def slider_value_changed(self):
        # 更新标签显示当前滑动条的值
        total_second_label = self._model.player.total_second  # 总时长不变
        self._model.player.start_second = self._view.horizontalSlider.value()
        # 更新音乐起始时间
        label_str = seconds_to_time(self._model.player.start_second) + '/' + seconds_to_time(total_second_label)
        self._view.label_progress.setText(label_str)
        # 播至最后
        if self._model.player.start_second == self._model.player.total_second:
            self.update_pre_play(next_music_idx=-1)  # 播放下一首

    def music_pause(self):
        # 更改play按钮字样
        self._view.pushButton_play.setText("播放")
        # 计时器暂停
        self._model.timer.stop()
        # 音乐暂停
        self._model.player.pause()

    def music_start(self):
        # 更改play按钮字样
        self._view.pushButton_play.setText("暂停")
        # 计时器继续
        self._model.timer.start(1000)
        # 音乐继续
        self._model.player.play()

    def change_buttons_state(self, target_state):
        self._view.horizontalSlider.setEnabled(target_state)
        # 更改按钮状态
        self._view.pushButton_pre.setEnabled(target_state)
        self._view.pushButton_play.setEnabled(target_state)
        self._view.pushButton_next.setEnabled(target_state)

    def click_on_play_button(self):
        if self._view.pushButton_play.text() == "播放":
            self.music_start()
        elif self._view.pushButton_play.text() == "暂停":
            self.music_pause()

    @pyqtSlot(dict)
    def update_view(self, datas):  # 更新界面内容
        if datas.get("music_base_path"):  # 更新歌单目录
            self._view.lineEdit.setText(self._model.music_base_path)
        if datas.get("music_list"):  # 更新歌曲列表
            self._view.listWidget.clear()  # 清空列表
            self._view.listWidget.addItems(self._model.music_list)
        if datas.get("information"):  # 显示警告
            self.msg_box.setText(datas.get("information")["message"])
            if datas.get("information")["code"] == 0:  # 通知
                self.msg_box.setIcon(QMessageBox.Information)
            elif datas.get("information")["code"] == 1:  # 警告
                self.msg_box.setIcon(QMessageBox.Warning)
            self.msg_box.exec_()  # 显示弹窗
        if datas.get("play"):  # 播放音乐
            self.play()  # 执行音乐播放流程
        if datas.get("timer_timeout"):  # 定时器信号
            self._model.player.start_second += 1
            self._view.horizontalSlider.setValue(self._model.player.start_second)
