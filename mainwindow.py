# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QDialog
from PyQt5.QtSql import QSqlTableModel




from Ui_mainwindow import Ui_MainWindow
from Ui_aboutdialog import Ui_Dialog
import db


class MainWindow(QMainWindow, Ui_MainWindow):
  
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        db.dbConnect()
        model = QSqlTableModel()
        db.readTable(model)
        self.listView.setModel(model)
        self.listView.setModelColumn(1)

    
        
    
    @pyqtSlot()
    def on_actionKilepes_triggered(self):
        result = QMessageBox.question(self,
                      "Kilépés megerősítése...",
                      "Biztosan ki akar lépni az programból?",
                      QMessageBox.Yes| QMessageBox.No, QMessageBox.No)
        if result == QMessageBox.Yes:
            #db.dbDisconnect()
            self.close()
    
    @pyqtSlot()
    def on_actionNevjegy_triggered(self):
        Dialog = QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.exec()
    
    @pyqtSlot()
    def on_actionUj_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: új bejegyzés létrehozása
        raise NotImplementedError
    
    @pyqtSlot()
    def on_actionMasolas_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: Másolás lekódolása
        raise NotImplementedError
    
    @pyqtSlot()
    def on_actionKivagas_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: Kivágás lekódolása
        raise NotImplementedError
    
    @pyqtSlot()
    def on_actionBeillesztes_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: Beillesztés funkció
        raise NotImplementedError
    
    @pyqtSlot()
    def on_actionMentes_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: Mentés funkció
        raise NotImplementedError
    
    @pyqtSlot()
    def on_actionMentes_maskent_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: Mentés másként
        raise NotImplementedError
    
    @pyqtSlot()
    def on_actionTorles_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: Törlés
        raise NotImplementedError
