import PyQt5.QtCore
from PyQt5.QtSql import *
from PyQt5 import QtSql


def dbConnect():
	db = QSqlDatabase.addDatabase("QSQLITE")
	filename = "db"
	database = PyQt5.QtCore.QFile(filename)
	if not database.exists():
		PyQt5.QtCore.qDebug("Database not found. Creating and opening")
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
		PyQt5.QtCore.qDebug("Database found. Opening")
		db.setDatabaseName(filename)
		db.open()
	return db.isOpen()

def dbClose():
	db = QSqlDatabase.addDatabase("QSQLITE")
	if db.isOpen():
		db.close()

def readTable(model):
	model.setTable('Bejegyzes')
	model.setEditStrategy(QtSql.QSqlTableModel.OnRowChange)
	model.select()
	return model

# def computeHash(original):
#    return QCryptographicHash.hash(QString(original).toUtf8(), QCryptographicHash.Md5).toHex()
