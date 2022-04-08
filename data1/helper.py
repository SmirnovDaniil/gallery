import os
import os.path
from data1.model import Image
#from PyQt5.QtCore import QObject, pyqtSlot, QVariant


def fill_table(path):
    for root, dirs, files in os.walk(path):
        imgs = [file for file in files if file.endswith('.jpg')]
        print(imgs)
        for i in imgs:
            Image.create(path=os.path.join(root, i), desc='123')

