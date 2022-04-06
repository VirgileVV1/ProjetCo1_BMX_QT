# This Python file uses the following encoding: utf-8

from Vue.mainwindow_ui import Ui_MainWindow
from PyQt6 import QtGui
from PyQt6 import QtCore
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import  QGraphicsDropShadowEffect

"""
 /!\ explication de pourquoi MainWindowSecond étend la classe Ui_MainWindow /!\
Ui_MainWindow contient tous les éléments de la fenetre de design, mais elle ne peut pas être modifiée car elle est obtenue en
compilant le fichier form.ui donc on l'écrase a chaque fois.
On utilise donc la classe MainWindowSecond pour accéder a tous les éléments de la classe Ui_MainWindow.
"""
class MainWindowSecond(Ui_MainWindow):
    def __init__(self, MainWindow):
        super().setupUi(MainWindow)
        # ajout du logo dans le label
        self.lblLogo.setPixmap(QtGui.QPixmap("./img/logo.svg"))

        # ajout de l'ombre en desous du header
        shadowEffect = QGraphicsDropShadowEffect( offset=QtCore.QPointF(3, 3), blurRadius=50, color=QColor("#9E9E9E"))
        self.widHeader.setGraphicsEffect(shadowEffect)

        # On connecte les boutons
        self.btnClubs.clicked.connect(lambda: self.swapWidget("Clubs"))
        self.btnTitulaires.clicked.connect(lambda: self.swapWidget("Titulaires"))
        self.btnChampionnats.clicked.connect(lambda: self.swapWidget("Championnats"))
        self.btnDeconnexion.clicked.connect()

    def swapWidget(self, name):
        if (name=="Clubs"):
            self.widStacked.setCurrentWidget(self.widClubs)
        elif (name=="Titulaires"):
            self.widStacked.setCurrentWidget(self.widTitulaires)
        elif (name=="Championnats"):
            self.widStacked.setCurrentWidget(self.widChampionnats)
