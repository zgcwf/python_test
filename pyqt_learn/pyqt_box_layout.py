import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QGroupBox, QRadioButton


# class MyWindowV(QWidget):
#     def __init__(self):
#         # 切记一定要调用父类的__init__方法，因为它里面有很多对UI空间的初始化操作
#         super().__init__()
#
#         # 设置大小
#         self.resize(600, 600)
#         # 设置标题
#         self.setWindowTitle("垂直布局")
#
#         # 垂直布局
#         # 创建布局器
#         layout = QVBoxLayout()
#
#         # 作用是在布局器中增加一个伸缩量，里面的参数表示QSpacerItem的个数, 默认值为0
#         # 会将你放在layout中的空间压缩成默认的大小
#         # 下面的笔试1：1：1：2
#         # 添加一个伸缩器
#         layout.addStretch(1)
#
#         # 按钮1
#         btn1 = QPushButton("按钮1")
#         # 添加到布局器中,这样可以不在设置当前ui的父窗口
#         layout.addWidget(btn1)
#
#         # 添加一个伸缩器
#         layout.addStretch(1)
#
#         # 按钮2
#         btn2 = QPushButton("按钮2")
#         # 添加到布局器
#         layout.addWidget(btn2)
#
#         # 添加一个伸缩器
#         layout.addStretch(1)
#
#         # 按钮3
#         btn3 = QPushButton("按钮3")
#         # 添加到布局器
#         layout.addWidget(btn3)
#
#         # 添加一个伸缩器
#         layout.addStretch(2)
#
#         # 让当前窗口使用这个排列的规则(布局去)
#         self.setLayout(layout)


class MyWindowH(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(600, 600)
        self.setWindowTitle("水平垂直布局")
        # 最外层的垂直布局，包含两部分：爱好和性别
        container = QVBoxLayout()

        # -----创建第1个组，添加多个组件-----
        # hobby 主要是保证他们是一个组。
        hobby_box = QGroupBox("爱好")
        # v_layout 垂直布局器
        v_layout = QVBoxLayout()
        # 爱好选项
        btn1 = QRadioButton("抽烟")
        btn2 = QRadioButton("喝酒")
        btn3 = QRadioButton("烫头")
        # 添加到v_layout中
        v_layout.addWidget(btn1)
        v_layout.addWidget(btn2)
        v_layout.addWidget(btn3)
        # hobby_box使用v_layout布局器
        hobby_box.setLayout(v_layout)

        # -----创建第2个组，添加多个组件-----
        # 性别组
        gender_box = QGroupBox("性别")
        # h_layout 水平布局器
        h_layout = QHBoxLayout()
        # 性别选项
        btn4 = QRadioButton("男")
        btn5 = QRadioButton("女")
        # 追加到性别容器中
        h_layout.addWidget(btn4)
        h_layout.addWidget(btn5)
        # gender_box容器使用水平布局器
        gender_box.setLayout(h_layout)

        # 把爱好的内容添加到容器中
        container.addWidget(hobby_box)
        # 把性别的内容添加到容器中
        container.addWidget(gender_box)
        # 设置窗口显示的内容是最外层容器
        self.setLayout(container)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 创建一个QWidget子类
    # wv = MyWindowV()
    # wv.show()

    # 创建一个QWidget子类
    wh = MyWindowH()
    wh.show()

    app.exec()
