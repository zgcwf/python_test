import sys
import time

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.init_ui()
#
#     def init_ui(self):
#         # 更改当前Widget的宽高
#         self.resize(500, 300)
#         # 创建一个按钮
#         btn = QPushButton("点我点我", self)
#         # 设置窗口位置、宽高
#         btn.setGeometry(200, 200, 100, 30)
#         # 将按钮被点击时触发的信号与我们定义的函数（方法）进行绑定
#         # 注意：这里没有()，即写函数的名字，而不是名字()
#         btn.clicked.connect(self.click_my_btn)
#
#     def click_my_btn(self, arg):
#         # 槽函数，点击按钮则调用该函数
#         # 这里的参数正好是信号发出，传递的参数
#         print("点击按钮啦~", arg, self)


# 自定义信号
class MyWindow(QWidget):
    # 自定义信号: 声明一个信号 只能放在函数的外面
    my_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.msg_history = list()  # 用来存放消息

    def init_ui(self):
        self.resize(500, 300)

        # 创建一个整体布局器
        container = QVBoxLayout()

        # 用来显示检测到漏洞的信息
        self.msg = QLabel("")
        self.msg.resize(440, 15)
        # print(self.msg.frameSize())
        self.msg.setWordWrap(True)  # 自动换行
        self.msg.setAlignment(Qt.AlignTop)  # 靠上
        # self.msg.setStyleSheet("background-color: yellow; color: black;")

        # 创建一个滚动对象
        scroll = QScrollArea()
        scroll.setWidget(self.msg)

        # 创建垂直布局器，用来添加自动滚动条
        v_layout = QVBoxLayout()
        v_layout.addWidget(scroll)

        # 创建水平布局器
        h_layout = QHBoxLayout()
        btn = QPushButton("开始检测", self)
        # 绑定按钮的点击，点击按钮则开始检测
        btn.clicked.connect(self.check)
        h_layout.addStretch(1)  # 伸缩器
        h_layout.addWidget(btn)
        h_layout.addStretch(1)

        # 操作将要显示的控件以及子布局器添加到container
        container.addLayout(v_layout)
        container.addLayout(h_layout)

        # 设置布局器
        self.setLayout(container)

        # 绑定信号和槽
        self.my_signal.connect(self.my_slot)

    def my_slot(self, msg):
        # 更新内容
        print('>>>', msg)
        self.msg_history.append(msg)
        self.msg.setText("<br>".join(self.msg_history))
        self.msg.resize(440, self.msg.frameSize().height() + 15)
        self.msg.repaint()  # 更新内容，如果不更新可能没有显示新内容

    def check(self):
        for i, ip in enumerate(["192.168.1.%d" % x for x in range(1, 255)]):
            msg = "模拟，正在检查 %s 上的漏洞...." % ip
            print(msg)
            if i % 5 == 3:
                # 表示发射信号 对象.信号.发射(参数)
                self.my_signal.emit(msg + "【发现漏洞】")
            time.sleep(0.01)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    app.exec()
