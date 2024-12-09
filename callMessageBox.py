from PyQt5 import QtWidgets

import datetime

def callInfoMessageBox(errorMessage: str = "Готово!", errorTitle: str = "Готово!"):
    messageBox = QtWidgets.QMessageBox()
    messageBox.setIcon(QtWidgets.QMessageBox.Icon.Information)
    messageBox.setWindowTitle(errorTitle)
    messageBox.setText(errorMessage)
    messageBox.exec()
    return

def callErrorMessageBox(errorMessage: str = "Ошибка!", errorTitle: str = "Ошибка!"):
    messageBox = QtWidgets.QMessageBox()
    messageBox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
    messageBox.setWindowTitle(errorTitle)
    messageBox.setText(errorMessage)
    messageBox.exec()
    return