from PyQt5 import QtCore, QtGui, QtWidgets
from settingsUI import Ui_SettingsWindow 
from config import Config

import settingsButtons

class SettingsWindow(QtWidgets.QMainWindow, Ui_SettingsWindow):
    def __init__(self, parent: QtWidgets.QMainWindow, initConfig: Config):
        super().__init__(parent)
        self.setupUi(self)
        
        self.listNameOfDirectionOfStudySettings.addItems(initConfig.directionsOfStudy)

        for i in range(0, len(initConfig.typesOfPractice)):
            self.listNameOfTypeOfPracticeSettings.addItem(initConfig.typesOfPractice[i]["type"])
            self.listDurationOfPracticeSettings.addItem(initConfig.typesOfPractice[i]["duration"])
        
        self.listNameOfDirectionOfStudySettings.itemClicked.connect(lambda: settingsButtons.unlockDeleteDirectionOfStudyButton(self.pushButtonDeleteSelectedDirectionOfStudySettings))
        
        self.listNameOfTypeOfPracticeSettings.itemClicked.connect(lambda: settingsButtons.listNameOfTypeOfPracticeSettingsItemClicked(self.listNameOfTypeOfPracticeSettings.currentRow(), self.listDurationOfPracticeSettings))
        self.listNameOfTypeOfPracticeSettings.itemClicked.connect(lambda: settingsButtons.unlockDeleteTypeOfPracticeButton(self.pushButtonDeleteSelectedTypeOfPracticeSettings))

        self.listDurationOfPracticeSettings.itemClicked.connect(lambda: settingsButtons.listlistDurationOfPracticeSettingsItemClicked(self.listDurationOfPracticeSettings.currentRow(), self.listNameOfTypeOfPracticeSettings))
        self.listDurationOfPracticeSettings.itemClicked.connect(lambda: settingsButtons.unlockDeleteTypeOfPracticeButton(self.pushButtonDeleteSelectedTypeOfPracticeSettings))

        self.pushButtonDeleteSelectedDirectionOfStudySettings.clicked.connect(lambda: settingsButtons.deleteDirectionOfStudy(self.listNameOfDirectionOfStudySettings))
        self.pushButtonAddNewDirectionOfStudySettings.clicked.connect(lambda: settingsButtons.addDirectionOfStudy(self.listNameOfDirectionOfStudySettings, self.lineEditNameOfNewDirectionOfStudySettings))
        
        self.pushButtonDeleteSelectedTypeOfPracticeSettings.clicked.connect(lambda: settingsButtons.deleteTypeOfPractice(self.listNameOfTypeOfPracticeSettings, self.listDurationOfPracticeSettings))
        self.pushButtonAddNewTypeOfPracticeSettings.clicked.connect(lambda: settingsButtons.addTypeOfPractice(self.listNameOfTypeOfPracticeSettings, self.listDurationOfPracticeSettings, self.lineEditNameOfNewTypeOfPracticeSettings, self.lineEditNewDurationOfPracticeSettings))

        self.show() 

    
