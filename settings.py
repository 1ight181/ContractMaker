from PyQt5 import QtWidgets
from settingsUI import Ui_SettingsWindow 
from config import Config

import settingsButtons

class SettingsWindow(QtWidgets.QMainWindow, Ui_SettingsWindow):
    def __init__(self, parent: QtWidgets.QMainWindow):
        super().__init__(parent)
        self.main = parent
        self.setupUi(self)
        self.setWindowModality(1)

        initConfig = Config()

        self.pushButtonApplyNameOfOrganization.setEnabled(initConfig.isCreateContractForOrganization)

        self.listNameOfDirectionOfStudySettings.addItems(initConfig.directionsOfStudy)
        self.lineEditNameOfOrganization.setText(initConfig.nameOfOrganization)

        self.checkBoxIsCreateContractForOrganization.setChecked(initConfig.isCreateContractForOrganization)
        
        for i in range(0, len(initConfig.typesOfPractice)):
            self.listNameOfTypeOfPracticeSettings.addItem(initConfig.typesOfPractice[i]["type"])
            self.listDurationOfPracticeSettings.addItem(initConfig.typesOfPractice[i]["duration"])

        del initConfig
        
        self.listNameOfDirectionOfStudySettings.itemClicked.connect(lambda: settingsButtons.unlockDeleteDirectionOfStudyButton(self.pushButtonDeleteSelectedDirectionOfStudySettings))
        
        self.listNameOfTypeOfPracticeSettings.itemClicked.connect(lambda: settingsButtons.listNameOfTypeOfPracticeSettingsItemClicked(self.listNameOfTypeOfPracticeSettings.currentRow(), 
                                                                                                                                      self.listDurationOfPracticeSettings))
        self.listNameOfTypeOfPracticeSettings.itemClicked.connect(lambda: settingsButtons.unlockDeleteTypeOfPracticeButton(self.pushButtonDeleteSelectedTypeOfPracticeSettings))

        self.listDurationOfPracticeSettings.itemClicked.connect(lambda: settingsButtons.listlistDurationOfPracticeSettingsItemClicked(self.listDurationOfPracticeSettings.currentRow(), 
                                                                                                                                      self.listNameOfTypeOfPracticeSettings))
        self.listDurationOfPracticeSettings.itemClicked.connect(lambda: settingsButtons.unlockDeleteTypeOfPracticeButton(self.pushButtonDeleteSelectedTypeOfPracticeSettings))

        self.pushButtonDeleteSelectedDirectionOfStudySettings.clicked.connect(lambda: settingsButtons.deleteDirectionOfStudy(self.listNameOfDirectionOfStudySettings))
        self.pushButtonAddNewDirectionOfStudySettings.clicked.connect(lambda: settingsButtons.addDirectionOfStudy(self.listNameOfDirectionOfStudySettings, 
                                                                                                                  self.lineEditNameOfNewDirectionOfStudySettings))
        
        self.pushButtonDeleteSelectedTypeOfPracticeSettings.clicked.connect(lambda: settingsButtons.deleteTypeOfPractice(self.listNameOfTypeOfPracticeSettings, 
                                                                                                                         self.listDurationOfPracticeSettings))
        self.pushButtonAddNewTypeOfPracticeSettings.clicked.connect(lambda: settingsButtons.addTypeOfPractice(self.listNameOfTypeOfPracticeSettings, 
                                                                                                              self.listDurationOfPracticeSettings, 
                                                                                                              self.lineEditNameOfNewTypeOfPracticeSettings, 
                                                                                                              self.lineEditNewDurationOfPracticeSettings))
        self.pushButtonApplyNameOfOrganization.clicked.connect(lambda: settingsButtons.applyNameOfOrganization(self.lineEditNameOfOrganization,
                                                                                                               self.pushButtonApplyNameOfOrganization))
        
        self.lineEditNameOfOrganization.textChanged.connect(lambda: self.pushButtonApplyNameOfOrganization.setEnabled(True))

        self.checkBoxIsCreateContractForOrganization.stateChanged.connect(lambda: Config.changeIsCreateContractForOrganization())
        
        self.show() 

    def closeEvent(self, event):
        newConfig = Config()
        self.main.nameOfOrganization = newConfig.nameOfOrganization
        self.main.isCreateContractForOrganization = newConfig.isCreateContractForOrganization
        self.main.directionsOfStudyParagraph = newConfig.directionsOfStudyParagraph
        self.main.typesOfPracticeParagraph = newConfig.typesOfPracticeParagraph

        self.main.comboBoxDirectionOfStudy.clear()

        self.main.comboBoxDirectionOfStudy.addItems(newConfig.directionsOfStudy)

        self.main.comboBoxTypeOfPractice.clear()
        self.main.comboBoxDurationOfPractice.clear()

        for i in range(0, len(newConfig.typesOfPractice)):
            self.main.comboBoxTypeOfPractice.addItem(newConfig.typesOfPractice[i]["type"])
            self.main.comboBoxDurationOfPractice.addItem(newConfig.typesOfPractice[i]["duration"])
    
