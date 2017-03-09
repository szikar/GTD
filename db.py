from PyQt5.QtCore import *
from PyQt5.QtSql import *
from PyQt5 import QtSql
 
def dbConnect():
    db = QSqlDatabase.addDatabase("QSQLITE")
    filename = "db"
    database =  QFile(filename)
    if not database.exists():
        qDebug("Database not found. Creating and opening")
        db.setDatabaseName(filename)
        db.open()
#        query = QSqlQuery()
#        query.exec_("create table qtapp_users "
#                    "(id integer primary key autoincrement, "
#                    "username varchar(30), "
#                    "password varchar(255))")
#        query.prepare("insert into qtapp_users(username, password) values(:username, :password)")
#        query.bindValue(":username", "eko")
#        query.bindValue(":password", computeHash("password"))
#        query.exec_()
    else:
        qDebug("Database found. Opening")
        db.setDatabaseName(filename)
        db.open()
    return db.isOpen()

#TODO: Az adatbázis disconnectet meg kell csinálni, ne maradjon nyitva
# def dbDisconnect():
#     db.close()

def readTable(model):
        model.setTable('Bejegyzes')
        model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        model.select()
        return model

#def computeHash(original):
#    return QCryptographicHash.hash(QString(original).toUtf8(), QCryptographicHash.Md5).toHex()
