import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QDesktopWidget

print(sys.argv)
if __name__ == '__main__':
    # 创建应用对象(有且只有一个)
    # sys.argv: 将运行时的命令参数传递给QApplication
    app = QApplication(sys.argv)

    # 创建一个窗口对象
    w = QWidget()
    # 设置窗口位置和大小
    w.resize(800, 500)
    # w.move(300, 300)
    # w.setGeometry(800, 400, 1000, 800)
    # 调整窗口在屏幕中央显示
    center_pointer = QDesktopWidget().availableGeometry().center()
    x = center_pointer.x()
    y = center_pointer.y()
    old_x, old_y, width, height = w.frameGeometry().getRect()
    w.move(int(x - width / 2), int(y - height / 2))
    # 设置窗口标题
    w.setWindowTitle('Hello World')
    # 设置图标
    w.setWindowIcon(QIcon('icon..png'))

    # 下面创建一个Label（纯文本），在创建的时候指定了父对象
    label = QLabel("账号: ", w)
    # 显示文本的位置与大小 ： x, y , w, h
    label.setGeometry(20, 25, 50, 25)

    # 文本框
    edit = QLineEdit(w)
    edit.setPlaceholderText("请输入账号")
    edit.setGeometry(80, 25, 200, 25)

    # 在窗口里面添加按钮控件
    btn = QPushButton("登录")
    # 设置按钮的父亲是当前窗口，等于是添加到窗口中显示
    btn.setParent(w)
    # 显示位置与大小 ： x, y , w, h
    btn.setGeometry(100, 200, 100, 30)

    # 展示窗口
    w.show()

    # 程序进行循环等待状态,即程序开始运行,直到关闭了窗口
    sys.exit(app.exec_())
