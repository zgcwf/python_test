import QtQuick 2.0
import QtQuick.Window 2.2
import QtQuick.Controls 2.5

Window {
    visible : true // 设置窗口可见性为 true，这样窗口将在应用程序运行时显示出来。
    width: 640; height: 360 // 设置窗口的宽度和高度
    title: 'Hello World'
    color: "lightblue" // 设置窗口的背景颜色为浅蓝色

    property int buttonMargin: 4

    Text {
        id: txt
        text: "Hello World"
        font.pixelSize: 36
        anchors.centerIn: parent
    }

    Button
    {
        id:myButton
        text:"退出"
        anchors.left:parent.left
        anchors.leftMargin:buttonMargin
        anchors.bottom:parent.bottom
        anchors.bottomMargin:buttonMargin

        onClicked:{
            Qt.quit()
        }

        function slotDouble(){
            Qt.quit()
        }

        onDoubleClicked: {
            myButton.slotDouble()
        }
    }

    Button
    {
        id:myButton2
        x: 10  // 设置按钮的横坐标
        y: 10 // 设置纵坐标

        //安妮添加图标
        icon.source: "../pyqt_learn/icon.png"
        icon.color: "transparent"
        display: AbstractButton.TextUnderIcon
        text:"保存"

        //设置按钮背景颜色
        background: Rectangle {
            color: '#fff'
        }
    }
}

