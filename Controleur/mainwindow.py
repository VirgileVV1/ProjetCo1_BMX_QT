# This Python file uses the following encoding: utf-8

from Vue.mainwindow_ui import Ui_MainWindow


"""
 /!\ explication de pourquoi MainWindowSecond étend la classe Ui_MainWindow /!\
Ui_MainWindow contient tous les éléments de la fenetre de design, mais elle ne peut pas être modifiée car elle est obtenue en
compilant le fichier form.ui donc on l'écrase a chaque fois.
On utilise donc la classe MainWindowSecond pour accéder a tous les éléments de la classe Ui_MainWindow.
"""
class MainWindowSecond(Ui_MainWindow):
    def __init__(self, MainWindow):
        super().setupUi(MainWindow)
        print("non")
        self.pushButton_3.setText("oui")
        self.btnClubs.clicked.connect(lambda: self.swapWidget("1"))
        self.btnTitulaires.clicked.connect(lambda: self.swapWidget("2"))
        self.btnChampionnats.clicked.connect(lambda: self.swapWidget("3"))

    def swapWidget(self, nb):
        if (nb=="1"):
            self.widStacked.setCurrentWidget(self.widClubs)
        elif (nb=="2"):
            self.widStacked.setCurrentWidget(self.widTitulaires)
        else:
            self.widStacked.setCurrentWidget(self.widChampionnats)
