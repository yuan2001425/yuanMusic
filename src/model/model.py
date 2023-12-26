# -*- coding: utf-8 -*-
# @Time: 2023/12/25 下午2:43
# @Author: yuan425
# @Software: PyCharm

import os

from PyQt5.QtCore import pyqtSignal, QThread, QUrl, QTimer
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent


class AudioPlayer:
    def __init__(self):
        # 创建 QMediaPlayer 和 QMediaContent
        self.media_player = QMediaPlayer()

        self.speed = 1.0  # 0.5x/1.0x/1.5x/2.0x

        self.start_second = 0  # 默认从头开始（秒）
        self.total_second = None  # 音乐总时长（秒）

    def load(self, file_path):
        self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(file_path)))
        # 等待媒体状态变为 LoadedMedia
        self.media_player.mediaStatusChanged.connect(self.get_duration)
        self.media_player.setPlaybackRate(self.speed)

    def get_duration(self):
        # 获取音频总时长
        self.total_second = int(self.media_player.duration() / 1000)  # 获取总时长（单位秒）
        # 可以在此断开连接，避免重复获取
        self.media_player.mediaStatusChanged.disconnect(self.get_duration)

    def play(self):  # 播放
        self.media_player.setPosition(self.start_second * 1000)  # 单位毫秒
        self.media_player.play()

    def pause(self):  # 暂停
        self.media_player.pause()

    def stop(self):  # 停止
        self.media_player.stop()

    def change_speed(self):  # 改变速度
        self.media_player.setPlaybackRate(self.speed)


class Model(QThread):
    data_signal = pyqtSignal(dict)

    def __init__(self):
        super(QThread, self).__init__()

        self.pre_play = [-1, 0]  # 上一曲/当前
        self.music_base_path = os.getcwd()  # 歌单目录地址
        self.music_list = []  # 歌曲列表

        self.player = AudioPlayer()  # 歌曲播放实例

        # 创建一个定时器
        self.timer = QTimer(self)
        self.timer.timeout.connect(lambda: self.emit_data(timer_timeout=True))

    def initial_music(self):
        # 获取当前歌曲
        music_file = os.path.join(self.music_base_path, self.music_list[self.pre_play[1]])
        self.player.load(music_file)  # 加载音乐
        self.emit_data(information={
            "message": f"播放列表第{self.pre_play[1] + 1}首：\n{self.music_list[self.pre_play[1]]}：",
            "code": 0
        }, play=True)

    def emit_data(self, information=None, play=None, timer_timeout=None):
        """
        组装返回内容，与controller交互
        :param information: 弹框内容
        :param play: 播放信号，传递播放顺序
        :param timer_timeout: 定时器信号
        :return: 组装的字典，以供返回
        """
        result = {
            "information": information,
            "play": play,
            "timer_timeout": timer_timeout
        }
        self.data_signal.emit(result)
