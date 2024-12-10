from PyQt5 import QtWidgets
from config import  Config
from callMessageBox import callErrorMessageBox
import re

findSpacesRegEx = re.compile('\s+')

def applyNameOfOrganization(lineEditNameOfOrganization: QtWidgets.QLineEdit,
                            pushButtonApplyNameOfOrganization: QtWidgets.QPushButton):
    if lineEditNameOfOrganization.text() == "" or re.match(r"\s+", lineEditNameOfOrganization.text()):
        callErrorMessageBox("Заполните поле названия. Название не может начинаться с пробела.")
        return
    re.sub(findSpacesRegEx, " ", Config.insertNameOfOrganization(lineEditNameOfOrganization.text()))
    pushButtonApplyNameOfOrganization.setEnabled(False)

def deleteDirectionOfStudy(listNameOfDirectionOfStudySettings: QtWidgets.QListWidget):
    currentRow = listNameOfDirectionOfStudySettings.currentRow()


    Config.deleteDirectionOfStudyFromConfig(listNameOfDirectionOfStudySettings.item(currentRow).text())

    if currentRow >= 0:
        listNameOfDirectionOfStudySettings.takeItem(currentRow)
      
def addDirectionOfStudy(listNameOfDirectionOfStudySettings: QtWidgets.QListWidget, 
                        lineEditNameOfNewDirectionOfStudySettings: QtWidgets.QLineEdit):
    if lineEditNameOfNewDirectionOfStudySettings.text() == "" or re.match(r"\s+", lineEditNameOfNewDirectionOfStudySettings.text()):
        callErrorMessageBox("Заполните поле названия. Название не может начинаться с пробела.")
        return

    item = re.sub(findSpacesRegEx, " ", lineEditNameOfNewDirectionOfStudySettings.text())

    listNameOfDirectionOfStudySettings.addItem(item)

    Config.insertNewDirectionOfStudyToConfig(item)

    lineEditNameOfNewDirectionOfStudySettings.clear()
    
def deleteTypeOfPractice(listNameOfTypeOfPracticeSettings: QtWidgets.QListWidget, 
                         listDurationOfPracticeSettings: QtWidgets.QListWidget):
    currentRow = listNameOfTypeOfPracticeSettings.currentRow()

    Config.deleteTypeOfPracticeFromConfig(listNameOfTypeOfPracticeSettings.item(currentRow).text())

    if currentRow >= 0:
        listNameOfTypeOfPracticeSettings.takeItem(currentRow)

    if currentRow >= 0:
        listDurationOfPracticeSettings.takeItem(currentRow)

def addTypeOfPractice(listNameOfTypeOfPracticeSettings: QtWidgets.QListWidget, 
                      listDurationOfPracticeSettings: QtWidgets.QListWidget, 
                      lineEditNameOfNewTypeOfPracticeSettings: QtWidgets.QLineEdit, 
                      lineEditNewDurationOfPracticeSettings: QtWidgets.QLineEdit ):
    if lineEditNameOfNewTypeOfPracticeSettings.text() == "" \
        or re.match(r"\s+", lineEditNameOfNewTypeOfPracticeSettings.text())  \
        or lineEditNewDurationOfPracticeSettings.text() == ""  \
        or re.match(r"\s+", lineEditNewDurationOfPracticeSettings.text()):

        callErrorMessageBox("Заполните поля названия и часов! Название и значение часов не может начинаться с пробела.")
        return
    
    itemTypeOfPractice = re.sub(findSpacesRegEx, " ", lineEditNameOfNewTypeOfPracticeSettings.text())
    itemDurationOfPractice = re.sub(findSpacesRegEx, " ", lineEditNewDurationOfPracticeSettings.text())

    listNameOfTypeOfPracticeSettings.addItem(itemTypeOfPractice)
    listDurationOfPracticeSettings.addItem(itemDurationOfPractice)

    Config.insertNewTypeOfPracticeToConfig(itemTypeOfPractice, itemDurationOfPractice)

    lineEditNameOfNewTypeOfPracticeSettings.clear()
    lineEditNewDurationOfPracticeSettings.clear()

def listNameOfTypeOfPracticeSettingsItemClicked(currentRow: int, 
                                                listDurationOfPracticeSettings: QtWidgets.QListWidget):
    listDurationOfPracticeSettings.setCurrentRow(currentRow)

def listlistDurationOfPracticeSettingsItemClicked(currentRow: int, 
                                                  listNameOfTypeOfPracticeSettings: QtWidgets.QListWidget):
    listNameOfTypeOfPracticeSettings.setCurrentRow(currentRow)

def unlockDeleteTypeOfPracticeButton(pushButtonDeleteSelectedTypeOfPracticeSettings: 
                                     QtWidgets.QPushButton):
    pushButtonDeleteSelectedTypeOfPracticeSettings.setEnabled(True)

def unlockDeleteDirectionOfStudyButton(pushButtonDeleteSelectedDirectionOfStudySettings: 
                                       QtWidgets.QPushButton):
    pushButtonDeleteSelectedDirectionOfStudySettings.setEnabled(True)