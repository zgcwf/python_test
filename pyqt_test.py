import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    # w.resize(250, 150)
    # w.move(300, 300)
    w.setGeometry(800, 400, 400, 300)  # 设置窗口位置和大小
    w.setWindowTitle('Hello World')
    w.show()

    sys.exit(app.exec_())
