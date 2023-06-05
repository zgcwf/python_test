import sys

from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QTimer, QObject, pyqtSignal

from time import strftime, localtime

# 创建应用程序对象
app = QGuiApplication(sys.argv)

# 创建 QML 引擎
qml_engine = QQmlApplicationEngine()

# 加载 QML 文件
qml_engine.load('test.qml')
qml_engine.quit.connect(app.quit)


class Backend(QObject):
    # 创建信号
    updated = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        # Define timer.
        self.timer = QTimer()
        self.timer.setInterval(100)  # msecs 100 = 1/10th sec
        self.timer.timeout.connect(self.update_time)
        self.timer.start()

    def update_time(self):
        # Pass the current time to QML.
        curr_time = strftime("%H:%M:%S", localtime())
        self.updated.emit(curr_time)


# Define our backend object, which we pass to QML.
backend = Backend()
qml_engine.rootObjects()[0].setProperty('backend', backend)

# Initial call to trigger first update. Must be after the setProperty to connect signals.
backend.update_time()

# 执行应用程序
sys.exit(app.exec_())
