import sys
import mainButtons

from PyQt5 import QtCore, QtGui, QtWidgets
from settings import SettingsWindow
from mainUI import Ui_MainWindow
from config import Config

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, initConfig: Config):
        super().__init__()
        self.setupUi(self)

        self.comboBoxDirectionOfStudy.setPlaceholderText("Не выбрано")
        self.comboBoxTypeOfPractice.setPlaceholderText("Не выбрано")
        self.comboBoxDurationOfPractice.setPlaceholderText("Не выбрано")

        self.comboBoxDirectionOfStudy.addItems(initConfig.directionsOfStudy)

        for i in range(0, len(initConfig.typesOfPractice)):
            self.comboBoxTypeOfPractice.addItem(initConfig.typesOfPractice[i]["type"])
            self.comboBoxDurationOfPractice.addItem(initConfig.typesOfPractice[i]["duration"])

        self.pushButtonOpenOrder.clicked.connect(lambda: mainButtons.openOrderButton(self.listNumberOfStudent, self.listNameOfStudent, self.listGroupOfStudent, self.listPlaceOfPractice, self.listHeadOfPractice, self.comboBoxDirectionOfStudy, self.comboBoxTypeOfPractice, self.comboBoxDurationOfPractice, self.pushButtonCreateContract, self.actionCreateContract))
        
        self.pushButtonCreateContract.clicked.connect(lambda: mainButtons.saveContractButton(self.listNumberOfStudent, self.listNameOfStudent, self.listGroupOfStudent, self.listPlaceOfPractice, self.listHeadOfPractice, self.comboBoxDirectionOfStudy, self.comboBoxTypeOfPractice, self.comboBoxDurationOfPractice))
        
        self.actionOpenSettingsWindow.triggered.connect(lambda: mainButtons.openSettingsWindow(self))
        self.actionOpenOrder.triggered.connect(lambda: mainButtons.openOrderButton(self.listNumberOfStudent, self.listNameOfStudent, self.listGroupOfStudent, self.listPlaceOfPractice, self.listHeadOfPractice, self.comboBoxDirectionOfStudy, self.comboBoxTypeOfPractice, self.comboBoxDurationOfPractice, self.pushButtonCreateContract, self.actionCreateContract))
        self.actionCreateContract.triggered.connect(lambda: mainButtons.saveContractButton(self.listNumberOfStudent, self.listNameOfStudent, self.listGroupOfStudent, self.listPlaceOfPractice, self.listHeadOfPractice, self.comboBoxDirectionOfStudy, self.comboBoxTypeOfPractice, self.comboBoxDurationOfPractice))

        self.show()    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    config = Config()
    mainWindow = MainWindow(config)
    sys.exit(app.exec())

