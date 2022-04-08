import QtQuick 2.15
import QtQuick.Controls 2.15


Rectangle{
    color : 'green'
    width: 300
    height: 300
    GridView {
        id: gridView
        //property var images: taker.getImages()

        anchors.fill: parent

        model: taker.getImages()

        cellWidth: 100
        cellHeight: 100

        delegate:
                Image {
                    id: i
                    width : 80
                    height: 80
                    source: modelData.path
                    fillMode: Image.PreserveAspectFit
                }
    }
}

