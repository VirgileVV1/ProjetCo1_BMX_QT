# This Python file uses the following encoding: utf-8
"""
from Controleur.MainWindowSecond import MainWindowSecond
from Vue.connectionWindow_ui import Ui_connectionWindow


class connectionWindow(Ui_connectionWindow):
    def __init__(self, MainWindow):
        self.mainw = MainWindow
        super().setupUi(MainWindow)
        self.btnConnexion.clicked.connect(lambda: self.onBtnConnectionClicked(MainWindow))

#    ##slot
    def onBtnConnectionClicked(self, MainWindow):
        if (connection(self.lndtNomUtilisateur.text(), self.lndtMdp.text())):
            #╔MainWindow.close()
            window = MainWindowSecond(MainWindow)
            MainWindow.show()
                
        else:
            self.lblErreurIdentifiants.setText("Les identifiants saisis sont incorrects, veuillez les ressaisir")

def connection(username, mdp):
    if (username == "ufolep" and mdp =="ufolep2021"):
        return True
    return False
"""

