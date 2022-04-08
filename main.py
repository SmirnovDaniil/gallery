import os.path
import sys
from PyQt5.QtCore import QUrl, QObject, pyqtSlot
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine
from data1.model import DataTaker
from data1.model import createTables, fill_table


class ComponentCacheManager(QObject):
    def __init__(self, engine):
        super(ComponentCacheManager, self).__init__()
        self.engine = engine

    @pyqtSlot()
    def clearComponentCache(self):
        self.engine.clearComponentCache()


if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        qml_doc_path = args[1]
        print("QMl document path:", qml_doc_path)
    else:
        print("QML document path not set")
        exit()
    if not os.path.isfile(qml_doc_path):
        print("QML document is not a file")
        exit()
    app = QApplication([])
    createTables()
    fill_table(os.curdir)
    engine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty('qml_path', qml_doc_path)
    ccm = ComponentCacheManager(engine)
    taker = DataTaker()
    engine.rootContext().setContextProperty('taker', taker)
    engine.rootContext().setContextProperty('ccm', ccm)
    engine.load('main.qml')
    sys.exit(app.exec_())
