# This Python file uses the following encoding: utf-8
import sys
from PyQt6 import QtWidgets
from Controleur.connectionWindow import connectionWindow
from Controleur.MainWindowSecond import MainWindowSecond
#from Controleur.mainwindow import MainWindowSecond

#print('__file__={0:<35} | __name__={1:<25} | __package__={2:<25}'.format(__file__,__name__,str(__package__)))

"""
Commande pour compiler le form.ui (design) en Ui_MainWindow.py (python)
pyuic6 -x Vue/form.ui -o Vue/mainwindow_ui.py

-> Attention pour lancer le programme il ne faut pas lancer la méthode main du
fichier mainwindow_ui.py mais bien celle qui se trouve dans ce fichier
"""


""" METHODE MAIN """

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    connWin = connectionWindow(MainWindow)
    MainWindow.show()
    
    sys.exit(app.exec())
    