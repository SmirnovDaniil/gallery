from peewee import SqliteDatabase
import os
from peewee import Model, TextField, CharField, ForeignKeyField
from PyQt5.QtCore import  QObject, pyqtSlot, QVariant

# from data1.helper import fill_table

db = SqliteDatabase('db')


class BaseModel(Model):
    class Meta:
        database = db


class Image(BaseModel):
    path = TextField()
    desc = TextField()


class Category(BaseModel):
    name = CharField()
    desc = TextField()
    color = TextField()


class ImgCat(BaseModel):
    img = ForeignKeyField(Image)
    cat = ForeignKeyField(Category)


def createTables():
    db.create_tables([Image, Category, ImgCat])


def fill_table(path):
    for root, dirs, files in os.walk(path):
        print(root, dirs, files)
        imgs = [file for file in files if file.endswith('.jpg') and root == '.']
        print(imgs)
        if len(imgs) > 0:
            print(imgs)
            for i in imgs:
                Image.create(path=os.path.join(path, i), desc='123')

       # for i in Image.select().dicts():
            #print(i)


class DataTaker(QObject):
    @pyqtSlot(result=list)
    def getImages(self):
        return [QVariant(x) for x in Image.select().dicts()]



