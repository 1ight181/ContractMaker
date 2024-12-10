import sys
import mainButtons

from PyQt5 import QtCore, QtWidgets
from mainUI import Ui_MainWindow
from config import Config

#именование переменных и функций в CapWords, 
#так как библиотека PyQt являющаяся основной в проекте использует этот метод именования

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, initConfig: Config):
        super().__init__()
        self.setupUi(self)

        self.comboBoxDirectionOfStudy.setPlaceholderText("Не выбрано")
        self.comboBoxTypeOfPractice.setPlaceholderText("Не выбрано")
        self.comboBoxDurationOfPractice.setPlaceholderText("Не выбрано")

        self.actionCreateContract.setEnabled(False)

        self.nameOfOrganization = initConfig.nameOfOrganization
        self.isCreateContractForOrganization = initConfig.isCreateContractForOrganization
        self.directionsOfStudyParagraph = initConfig.directionsOfStudyParagraph
        self.typesOfPracticeParagraph = initConfig.typesOfPracticeParagraph
        self.periodOfPracticeParagraph = initConfig.periodOfPracticeParagraph

        self.comboBoxDirectionOfStudy.addItems(initConfig.directionsOfStudy)

        for i in range(0, len(initConfig.typesOfPractice)):
            self.comboBoxTypeOfPractice.addItem(initConfig.typesOfPractice[i]["type"])
            self.comboBoxDurationOfPractice.addItem(initConfig.typesOfPractice[i]["duration"])
            
        del initConfig

        self.pushButtonOpenOrder.clicked.connect(lambda: mainButtons.openOrderButton(self.listNumberOfStudent, 
                                                                                     self.listNameOfStudent, 
                                                                                     self.listGroupOfStudent, 
                                                                                     self.listPlaceOfPractice, 
                                                                                     self.listHeadOfPractice, 
                                                                                     self.comboBoxDirectionOfStudy, 
                                                                                     self.comboBoxTypeOfPractice, 
                                                                                     self.comboBoxDurationOfPractice, 
                                                                                     self.lineEditNumberOfAuthority,
                                                                                     self.lineEditDateOfAuthority,
                                                                                     self.pushButtonCreateContract, 
                                                                                     self.actionCreateContract,
                                                                                     self.textEditPeriodOfPractice,
                                                                                     self.nameOfOrganization,
                                                                                     self.isCreateContractForOrganization,
                                                                                     self.directionsOfStudyParagraph,
                                                                                     self.typesOfPracticeParagraph,
                                                                                     self.periodOfPracticeParagraph
                                                                                     ))
        
        self.pushButtonCreateContract.clicked.connect(lambda: mainButtons.saveContractButton(self.listNameOfStudent, 
                                                                                             self.listGroupOfStudent, 
                                                                                             self.listPlaceOfPractice, 
                                                                                             self.comboBoxDirectionOfStudy, 
                                                                                             self.comboBoxTypeOfPractice, 
                                                                                             self.comboBoxDurationOfPractice,
                                                                                             self.lineEditNumberOfAuthority,
                                                                                             self.lineEditDateOfAuthority,
                                                                                             self.textEditPeriodOfPractice
                                                                                             ))
        
        self.actionOpenSettingsWindow.triggered.connect(lambda: mainButtons.openSettingsWindow(self))

        self.actionOpenOrder.triggered.connect(lambda: mainButtons.openOrderButton(self.listNumberOfStudent,
                                                                                   self.listNameOfStudent,
                                                                                   self.listGroupOfStudent,
                                                                                   self.listPlaceOfPractice,
                                                                                   self.listHeadOfPractice,
                                                                                   self.comboBoxDirectionOfStudy,
                                                                                   self.comboBoxTypeOfPractice,
                                                                                   self.comboBoxDurationOfPractice,
                                                                                   self.lineEditNumberOfAuthority,
                                                                                   self.lineEditDateOfAuthority,
                                                                                   self.pushButtonCreateContract,
                                                                                   self.actionCreateContract,
                                                                                   self.textEditPeriodOfPractice,
                                                                                   self.nameOfOrganization,
                                                                                   self.isCreateContractForOrganization,
                                                                                   self.directionsOfStudyParagraph,
                                                                                   self.typesOfPracticeParagraph,
                                                                                   self.periodOfPracticeParagraph
                                                                                   ))
        
        self.actionCreateContract.triggered.connect(lambda: mainButtons.saveContractButton(self.listNameOfStudent, 
                                                                                           self.listGroupOfStudent, 
                                                                                           self.listPlaceOfPractice, 
                                                                                           self.comboBoxDirectionOfStudy, 
                                                                                           self.comboBoxTypeOfPractice, 
                                                                                           self.comboBoxDurationOfPractice,
                                                                                           self.lineEditNumberOfAuthority,
                                                                                           self.lineEditDateOfAuthority,
                                                                                           self.textEditPeriodOfPractice
                                                                                           ))
    
        self.show()    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    config = Config()
    mainWindow = MainWindow(config)
    sys.exit(app.exec())

