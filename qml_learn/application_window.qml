import QtQuick 2.15
import QtQuick.Controls 1.6


ApplicationWindow {
    visible: true
    id: root_win
    width: 300
    height: 200
    title: "我是标题"

    Text {
        text: "Qt Quick"
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter
        font.pixelSize : 24
        font.bold: true
    }

    Button {
        x: 20
        y: 20
        text: "Quit"
        onClicked: Qt.quit()
    }

    function onChecked(checked) {
        root_win.title = checked ? "我是标题" : " "
    }

    CheckBox {
        x: 150
        y: 150
        text: "set title"
        checked: true
        onClicked: root_win.onChecked(checked)
    }

    Row {
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.bottom:parent.bottom
        anchors.bottomMargin:10
        spacing: 10

        Slider {
            id: slider
            minimumValue: 0
            maximumValue: 100
        }

        Label {
            text: Math.floor(slider.value)
            font.pixelSize : 16
        }
    }

    Rectangle {
        x: 20
        y: 20
        width: 100; height: 100
        color: "forestgreen"

        NumberAnimation on x { to: 250; duration: 1000 }
    }
}
