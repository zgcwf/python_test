import sys
from PyQt5 import QtWidgets, QtQml, QtCore

# 创建应用程序对象
app = QtWidgets.QApplication(sys.argv)

# 创建 QML 引擎
qml_engine = QtQml.QQmlApplicationEngine()

# 加载 QML 文件
qml_url = QtCore.QUrl('main.qml')
qml_engine.load(qml_url)
qml_engine.quit.connect(app.quit)

# 检查 QML 文件是否加载成功
if not qml_engine.rootObjects():
    sys.exit(-1)

# 显示窗口
window = qml_engine.rootObjects()[0]
window.show()

# 执行应用程序
sys.exit(app.exec_())
