# 远哥挺乐-音频播放器


*Click [here](README.md) to return to the English document*

这是一个基于 PyQt5 的音频播放器项目，采用了 MVC 框架。该项目在 Ubuntu 20.04 下进行开发，可指定播放特定文件夹下的歌曲及顺序播放、单曲循环、随机播放等基本功能。此外，还实现了倍速播放功能。

- 项目地址：https://github.com/yuan2001425/yuanMusic
- 演示视频：https://www.bilibili.com/video/BV1aa4y1B7WW
- 博客地址：https://yuan425.blog.csdn.net/article/details/135234255

## 环境配置

使用以下命令创建项目所需的虚拟环境：

```bash
conda env create -f environment.yml
conda activate yuanMusic
```

## 运行项目

**1. 准备音频文件**

可以选择创建一个空的 `music` 文件夹，然后自行添加音频文件：

```bash
mkdir music
```

或者解压所提供的示例音乐（陈奕迅流行曲）：

> 链接: https://pan.baidu.com/s/1EG0QBhtZ_KfbkuHmxejUeA?pwd=i9pz
> 
> 提取码: i9pz
> 
> --来自百度网盘超级会员v5的分享

```bash
unzip music.zip
```

**2. 配置音频文件类型（可选）**

打开 `src/controller/controller.py` 文件

修改 `ALLOW_VOICE_TYPE` 变量以允许播放其他文件类型，默认为：

```python
ALLOW_VOICE_TYPE = [".mp3", ".wav"]
```

**3. 启动音频播放器**

在终端中运行以下命令启动音频播放器：

```bash
python main.py
```

## 功能特性

- **指定文件夹播放：** 可以选择特定文件夹，仅播放该文件夹下的歌曲。
- **播放模式：** 支持顺序播放、单曲循环、随机播放。
- **倍速播放：** 提供倍速播放选项，以加快或减缓音频播放速度。

## 使用说明

1. **启动应用程序：**
   - 打开应用程序后，通过界面上的控件选择播放模式和目标文件夹。
   - 系统将自动检测目录中可以播放的音频文件，并显示在列表中。
   - 默认情况下，系统将自动播放列表中的第一首歌曲。

2. **音频播放控制：**
   - 点击播放按钮可实现音频的播放和暂停功能。
   - 通过拖动滑块可以轻松调整音频播放的进度。

3. **音频切换与调整：**
   - 使用上一曲、下一曲按钮或双击列表中的歌曲可以方便地切换音频。
   - 调整循环模式和播放倍速，以满足个性化需求。

4. **退出应用程序：**
   - 若要退出应用程序，只需点击窗口右上角的关闭按钮即可。

## 文件目录

- **doc**: 相关文档
- **music**: 示例音乐目录
- **src**: 源代码
  - **controller**: 控制逻辑
    - `controller.py`
  - **model**: 音频模型
    - `model.py`
  - **view**: 显示界面
    - **UI**: QtDesigner生成的UI界面
      - `Widget.py`
      - `Widget.ui`
    - `view.py`: 个性化前端
- `environment.yml`: 依赖安装
- `main.py`: 函数入口
- `README_CN.md`: 中文项目介绍
- `README.md`: 英文项目介绍

## 注意事项

- 请确保已安装 Python 3.10 或以上
- 在运行应用程序前，确保已经配置好环境并激活虚拟环境。

## 版本信息

- Python 版本：3.10
- PyQt 版本：5.15

## 作者信息

作者：`远哥挺乐`（CSDN/B站/GitHub/公众号同名）

如有任何问题或建议，请联系作者：`yuan2001425@163.com`
