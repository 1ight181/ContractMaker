from PyQt5 import QtWidgets
from config import  Config
from callMessageBox import callErrorMessageBox

def applyNameOfOrganization(lineEditNameOfOrganization: QtWidgets.QLineEdit,
                            pushButtonApplyNameOfOrganization: QtWidgets.QPushButton):
    if lineEditNameOfOrganization.text() == "":
        callErrorMessageBox("Заполните поле названия")
        return
    Config.insertNameOfOrganization(lineEditNameOfOrganization.text())
    pushButtonApplyNameOfOrganization.setEnabled(False)

def deleteDirectionOfStudy(listNameOfDirectionOfStudySettings: QtWidgets.QListWidget):
    currentRow = listNameOfDirectionOfStudySettings.currentRow()


    Config.deleteDirectionOfStudyFromConfig(listNameOfDirectionOfStudySettings.item(currentRow).text())

    if currentRow >= 0:
        listNameOfDirectionOfStudySettings.takeItem(currentRow)
      
def addDirectionOfStudy(listNameOfDirectionOfStudySettings: QtWidgets.QListWidget, lineEditNameOfNewDirectionOfStudySettings: QtWidgets.QLineEdit):
    if lineEditNameOfNewDirectionOfStudySettings.text() == "":
        callErrorMessageBox("Заполните поле названия")
        return

    listNameOfDirectionOfStudySettings.addItem(lineEditNameOfNewDirectionOfStudySettings.text())

    Config.insertNewDirectionOfStudyToConfig(lineEditNameOfNewDirectionOfStudySettings.text())

    lineEditNameOfNewDirectionOfStudySettings.clear()
    
def deleteTypeOfPractice(listNameOfTypeOfPracticeSettings: QtWidgets.QListWidget, listDurationOfPracticeSettings: QtWidgets.QListWidget):
    currentRow = listNameOfTypeOfPracticeSettings.currentRow()

    Config.deleteTypeOfPracticeFromConfig(listNameOfTypeOfPracticeSettings.item(currentRow).text())

    if currentRow >= 0:
        listNameOfTypeOfPracticeSettings.takeItem(currentRow)

    if currentRow >= 0:
        listDurationOfPracticeSettings.takeItem(currentRow)

def addTypeOfPractice(listNameOfTypeOfPracticeSettings: QtWidgets.QListWidget, listDurationOfPracticeSettings: QtWidgets.QListWidget, lineEditNameOfNewTypeOfPracticeSettings: QtWidgets.QLineEdit, lineEditNewDurationOfPracticeSettings: QtWidgets.QLineEdit ):
    if lineEditNameOfNewTypeOfPracticeSettings.text() == "" or lineEditNewDurationOfPracticeSettings.text() == "":
        callErrorMessageBox("Заполните поля названия и часов!")
        return
    
    listNameOfTypeOfPracticeSettings.addItem(lineEditNameOfNewTypeOfPracticeSettings.text())
    listDurationOfPracticeSettings.addItem(lineEditNewDurationOfPracticeSettings.text())

    Config.insertNewTypeOfPracticeToConfig(lineEditNameOfNewTypeOfPracticeSettings.text(), lineEditNewDurationOfPracticeSettings.text())

    lineEditNameOfNewTypeOfPracticeSettings.clear()
    lineEditNewDurationOfPracticeSettings.clear()

def listNameOfTypeOfPracticeSettingsItemClicked(currentRow: int, listDurationOfPracticeSettings: QtWidgets.QListWidget):
    listDurationOfPracticeSettings.setCurrentRow(currentRow)

def listlistDurationOfPracticeSettingsItemClicked(currentRow: int, listNameOfTypeOfPracticeSettings: QtWidgets.QListWidget):
    listNameOfTypeOfPracticeSettings.setCurrentRow(currentRow)

def unlockDeleteTypeOfPracticeButton(pushButtonDeleteSelectedTypeOfPracticeSettings: QtWidgets.QPushButton):
    pushButtonDeleteSelectedTypeOfPracticeSettings.setEnabled(True)

def unlockDeleteDirectionOfStudyButton(pushButtonDeleteSelectedDirectionOfStudySettings: QtWidgets.QPushButton):
    pushButtonDeleteSelectedDirectionOfStudySettings.setEnabled(True)