import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    id : root
    visible: true
    width:  300
    height: 300
    Component.onCompleted: {
        console.log("path in qml:",
        qml.path)
      }
    Loader{
        id: loader
        sourceComponent: Qt.createComponent(qml_path)
    }
    Shortcut{
        sequence: 'F5'
        onActivated: {
            loader.active = false
            ccm.clearComponentCache()
            let component = Qt.createComponent(qml_path)
            loader.sourceComponent = component
            loader.active = true
        }
    }
}
