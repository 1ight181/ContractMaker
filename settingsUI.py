# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settingsUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        SettingsWindow.setObjectName("SettingsWindow")
        SettingsWindow.resize(703, 412)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SettingsWindow.sizePolicy().hasHeightForWidth())
        SettingsWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SettingsWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(SettingsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 90, 331, 321))
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 30, 311, 285))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.labelAddNewDirectionOfStudySettings = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labelAddNewDirectionOfStudySettings.setObjectName("labelAddNewDirectionOfStudySettings")
        self.gridLayout.addWidget(self.labelAddNewDirectionOfStudySettings, 5, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelNewDirectionOfStudySettings = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labelNewDirectionOfStudySettings.setObjectName("labelNewDirectionOfStudySettings")
        self.horizontalLayout_3.addWidget(self.labelNewDirectionOfStudySettings)
        self.horizontalLayout_3.setStretch(0, 3)
        self.gridLayout.addLayout(self.horizontalLayout_3, 6, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.labelNameOfDirectionOfStudySettings = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labelNameOfDirectionOfStudySettings.setObjectName("labelNameOfDirectionOfStudySettings")
        self.horizontalLayout_4.addWidget(self.labelNameOfDirectionOfStudySettings)
        self.horizontalLayout_4.setStretch(0, 3)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listNameOfDirectionOfStudySettings = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.listNameOfDirectionOfStudySettings.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.listNameOfDirectionOfStudySettings.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.listNameOfDirectionOfStudySettings.setSelectionRectVisible(False)
        self.listNameOfDirectionOfStudySettings.setObjectName("listNameOfDirectionOfStudySettings")
        self.horizontalLayout.addWidget(self.listNameOfDirectionOfStudySettings)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.labelAllDirectionOfStudySettings = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labelAllDirectionOfStudySettings.setObjectName("labelAllDirectionOfStudySettings")
        self.gridLayout.addWidget(self.labelAllDirectionOfStudySettings, 0, 0, 1, 1)
        self.pushButtonDeleteSelectedDirectionOfStudySettings = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButtonDeleteSelectedDirectionOfStudySettings.setEnabled(False)
        self.pushButtonDeleteSelectedDirectionOfStudySettings.setObjectName("pushButtonDeleteSelectedDirectionOfStudySettings")
        self.gridLayout.addWidget(self.pushButtonDeleteSelectedDirectionOfStudySettings, 3, 0, 1, 1)
        self.pushButtonAddNewDirectionOfStudySettings = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButtonAddNewDirectionOfStudySettings.setObjectName("pushButtonAddNewDirectionOfStudySettings")
        self.gridLayout.addWidget(self.pushButtonAddNewDirectionOfStudySettings, 8, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEditNameOfNewDirectionOfStudySettings = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEditNameOfNewDirectionOfStudySettings.setReadOnly(False)
        self.lineEditNameOfNewDirectionOfStudySettings.setObjectName("lineEditNameOfNewDirectionOfStudySettings")
        self.horizontalLayout_2.addWidget(self.lineEditNameOfNewDirectionOfStudySettings)
        self.horizontalLayout_2.setStretch(0, 3)
        self.gridLayout.addLayout(self.horizontalLayout_2, 7, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(360, 90, 331, 321))
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_3)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 30, 311, 285))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.labelAddNewTypeOfPracticeSettings = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.labelAddNewTypeOfPracticeSettings.setObjectName("labelAddNewTypeOfPracticeSettings")
        self.gridLayout_2.addWidget(self.labelAddNewTypeOfPracticeSettings, 5, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.labelNewTypeOfPracticeSettings = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.labelNewTypeOfPracticeSettings.setObjectName("labelNewTypeOfPracticeSettings")
        self.horizontalLayout_5.addWidget(self.labelNewTypeOfPracticeSettings)
        self.labelNewDurationOfPracticeSettings = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.labelNewDurationOfPracticeSettings.setObjectName("labelNewDurationOfPracticeSettings")
        self.horizontalLayout_5.addWidget(self.labelNewDurationOfPracticeSettings)
        self.horizontalLayout_5.setStretch(0, 3)
        self.horizontalLayout_5.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 6, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.labelNameOfTypeOfPracticeSettings = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.labelNameOfTypeOfPracticeSettings.setObjectName("labelNameOfTypeOfPracticeSettings")
        self.horizontalLayout_6.addWidget(self.labelNameOfTypeOfPracticeSettings)
        self.labelDurationOfPracticeSettings = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.labelDurationOfPracticeSettings.setObjectName("labelDurationOfPracticeSettings")
        self.horizontalLayout_6.addWidget(self.labelDurationOfPracticeSettings)
        self.horizontalLayout_6.setStretch(0, 3)
        self.horizontalLayout_6.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.listNameOfTypeOfPracticeSettings = QtWidgets.QListWidget(self.gridLayoutWidget_2)
        self.listNameOfTypeOfPracticeSettings.setObjectName("listNameOfTypeOfPracticeSettings")
        self.horizontalLayout_7.addWidget(self.listNameOfTypeOfPracticeSettings)
        self.listDurationOfPracticeSettings = QtWidgets.QListWidget(self.gridLayoutWidget_2)
        self.listDurationOfPracticeSettings.setObjectName("listDurationOfPracticeSettings")
        self.horizontalLayout_7.addWidget(self.listDurationOfPracticeSettings)
        self.horizontalLayout_7.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.horizontalLayout_7, 2, 0, 1, 1)
        self.labelAllTypesOfPracticeSettings_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.labelAllTypesOfPracticeSettings_2.setObjectName("labelAllTypesOfPracticeSettings_2")
        self.gridLayout_2.addWidget(self.labelAllTypesOfPracticeSettings_2, 0, 0, 1, 1)
        self.pushButtonDeleteSelectedTypeOfPracticeSettings = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButtonDeleteSelectedTypeOfPracticeSettings.setEnabled(False)
        self.pushButtonDeleteSelectedTypeOfPracticeSettings.setObjectName("pushButtonDeleteSelectedTypeOfPracticeSettings")
        self.gridLayout_2.addWidget(self.pushButtonDeleteSelectedTypeOfPracticeSettings, 3, 0, 1, 1)
        self.pushButtonAddNewTypeOfPracticeSettings = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButtonAddNewTypeOfPracticeSettings.setObjectName("pushButtonAddNewTypeOfPracticeSettings")
        self.gridLayout_2.addWidget(self.pushButtonAddNewTypeOfPracticeSettings, 8, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lineEditNameOfNewTypeOfPracticeSettings = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEditNameOfNewTypeOfPracticeSettings.setReadOnly(False)
        self.lineEditNameOfNewTypeOfPracticeSettings.setObjectName("lineEditNameOfNewTypeOfPracticeSettings")
        self.horizontalLayout_8.addWidget(self.lineEditNameOfNewTypeOfPracticeSettings)
        self.lineEditNewDurationOfPracticeSettings = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEditNewDurationOfPracticeSettings.setObjectName("lineEditNewDurationOfPracticeSettings")
        self.horizontalLayout_8.addWidget(self.lineEditNewDurationOfPracticeSettings)
        self.horizontalLayout_8.setStretch(0, 3)
        self.horizontalLayout_8.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.horizontalLayout_8, 7, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 4, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 681, 81))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_2)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 651, 51))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineEditNameOfOrganization = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.lineEditNameOfOrganization.setInputMask("")
        self.lineEditNameOfOrganization.setText("")
        self.lineEditNameOfOrganization.setObjectName("lineEditNameOfOrganization")
        self.gridLayout_3.addWidget(self.lineEditNameOfOrganization, 0, 1, 1, 1)
        self.checkBoxIsCreateContractForOrganization = QtWidgets.QCheckBox(self.gridLayoutWidget_3)
        self.checkBoxIsCreateContractForOrganization.setCheckable(True)
        self.checkBoxIsCreateContractForOrganization.setChecked(False)
        self.checkBoxIsCreateContractForOrganization.setObjectName("checkBoxIsCreateContractForOrganization")
        self.gridLayout_3.addWidget(self.checkBoxIsCreateContractForOrganization, 1, 0, 1, 1)
        self.labelNameOfOrganization = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelNameOfOrganization.setFont(font)
        self.labelNameOfOrganization.setObjectName("labelNameOfOrganization")
        self.gridLayout_3.addWidget(self.labelNameOfOrganization, 0, 0, 1, 1)
        self.pushButtonApplyNameOfOrganization = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.pushButtonApplyNameOfOrganization.setObjectName("pushButtonApplyNameOfOrganization")
        self.gridLayout_3.addWidget(self.pushButtonApplyNameOfOrganization, 0, 2, 1, 1)
        SettingsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SettingsWindow)
        QtCore.QMetaObject.connectSlotsByName(SettingsWindow)

    def retranslateUi(self, SettingsWindow):
        _translate = QtCore.QCoreApplication.translate
        SettingsWindow.setWindowTitle(_translate("SettingsWindow", "Настройки"))
        self.groupBox.setTitle(_translate("SettingsWindow", "Добавление новых направлений"))
        self.labelAddNewDirectionOfStudySettings.setText(_translate("SettingsWindow", "Добавить новое:"))
        self.labelNewDirectionOfStudySettings.setText(_translate("SettingsWindow", "Название:"))
        self.labelNameOfDirectionOfStudySettings.setText(_translate("SettingsWindow", "Название:"))
        self.labelAllDirectionOfStudySettings.setText(_translate("SettingsWindow", "Список существующих направлений:"))
        self.pushButtonDeleteSelectedDirectionOfStudySettings.setText(_translate("SettingsWindow", "Удалить "))
        self.pushButtonAddNewDirectionOfStudySettings.setText(_translate("SettingsWindow", "Добавить"))
        self.groupBox_3.setTitle(_translate("SettingsWindow", "Добавление новых типов практики"))
        self.labelAddNewTypeOfPracticeSettings.setText(_translate("SettingsWindow", "Добавить новое:"))
        self.labelNewTypeOfPracticeSettings.setText(_translate("SettingsWindow", "Название:"))
        self.labelNewDurationOfPracticeSettings.setText(_translate("SettingsWindow", "Часы:"))
        self.labelNameOfTypeOfPracticeSettings.setText(_translate("SettingsWindow", "Название:"))
        self.labelDurationOfPracticeSettings.setText(_translate("SettingsWindow", "Часы:"))
        self.labelAllTypesOfPracticeSettings_2.setText(_translate("SettingsWindow", "Список существующих типов практики:"))
        self.pushButtonDeleteSelectedTypeOfPracticeSettings.setText(_translate("SettingsWindow", "Удалить "))
        self.pushButtonAddNewTypeOfPracticeSettings.setText(_translate("SettingsWindow", "Добавить"))
        self.groupBox_2.setTitle(_translate("SettingsWindow", "Образовательная организация"))
        self.checkBoxIsCreateContractForOrganization.setText(_translate("SettingsWindow", "Не создавать договора для практики внутри образовательной организации"))
        self.labelNameOfOrganization.setText(_translate("SettingsWindow", "Наименование образовательной организации:"))
        self.pushButtonApplyNameOfOrganization.setText(_translate("SettingsWindow", "Применить"))
