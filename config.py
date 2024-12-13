import yaml, callMessageBox

class Config:
    def __init__(self):
        try:
            with open("config.yaml") as f:
                config = yaml.safe_load(f)
            self.directionsOfStudy = config["directionsOfStudy"]
            self.typesOfPractice = config["typesOfPractice"]
            self.nameOfOrganization = config["nameOfOrganization"]
            self.isCreateContractForOrganization = config["isCreateContractForOrganization"]
            self.directionsOfStudyParagraph = config["directionsOfStudyParagraph"]
            self.typesOfPracticeParagraph = config["typesOfPracticeParagraph"]
            self.periodOfPracticeParagraph = config["periodOfPracticeParagraph"]
        except:
            try:
                with open("config-backup.yaml", "w") as f:
                    yaml.dump(config ,f, encoding='UTF-8', allow_unicode=True) 
            except:
                pass
        
            self.directionsOfStudy = []
            self.typesOfPractice = [{"type": "Учебная практика", "duration": '207'}]
            self.nameOfOrganization = "(отсутствует)"
            self.isCreateContractForOrganization = True
            self.directionsOfStudyParagraph = 14
            self.typesOfPracticeParagraph = 17
            self.periodOfPracticeParagraph = 17

            config = {"directionsOfStudy": self.directionsOfStudy,
                    "typesOfPractice": self.typesOfPractice,
                    "nameOfOrganization": self.nameOfOrganization,
                    "isCreateContractForOrganization": self.isCreateContractForOrganization,
                    "directionsOfStudyParagraph": self.directionsOfStudyParagraph,
                    "typesOfPracticeParagraph": self.typesOfPracticeParagraph,
                    "periodOfPracticeParagraph": self.periodOfPracticeParagraph} 
            
            callMessageBox.callErrorMessageBox("Ошибка конфигаратора! "  
                                            + "Конфигурационный файл возвращен к исходным настройкам. " 
                                            + "Копия старого конфигурационного файла сохраненна в config-backup.yaml")

            with open("config.yaml", "w") as f:
                yaml.dump(config ,f, encoding='UTF-8', allow_unicode=True)   

    @staticmethod
    def changeIsCreateContractForOrganization ():
        with open("config.yaml") as f:
            config = yaml.safe_load(f)
        
        config["isCreateContractForOrganization"] = not config["isCreateContractForOrganization"]

        with open("config.yaml", "w") as f:
            yaml.dump(config ,f, encoding='UTF-8', allow_unicode=True)
    
    @staticmethod
    def insertNameOfOrganization(newNameOfOrganization: str):
        with open("config.yaml") as f:
            config = yaml.safe_load(f)

        config["nameOfOrganization"] = newNameOfOrganization

        with open("config.yaml", "w") as f:
            yaml.dump(config ,f, encoding='UTF-8', allow_unicode=True)

    @staticmethod
    def insertNewDirectionOfStudyToConfig(newDirectionOfStudy: str):
        with open("config.yaml") as f:
            config = yaml.safe_load(f)

        config["directionsOfStudy"].append(newDirectionOfStudy)

        with open("config.yaml", "w") as f:
            yaml.dump(config ,f, encoding='UTF-8', allow_unicode=True)

    @staticmethod
    def deleteDirectionOfStudyFromConfig(directionOfStudy: str):
        with open("config.yaml") as f:
            config = yaml.safe_load(f)

        config["directionsOfStudy"].remove(directionOfStudy)

        with open("config.yaml", "w") as f:
            yaml.dump(config ,f, encoding='UTF-8', allow_unicode=True)

    @staticmethod
    def insertNewTypeOfPracticeToConfig(newTypeOfPractice: str, durationOfPractice: str):
        with open("config.yaml") as f:
            config = yaml.safe_load(f)

        config["typesOfPractice"].append({"type": newTypeOfPractice, "duration": durationOfPractice})

        with open("config.yaml", "w") as f:
            yaml.dump(config ,f, encoding='UTF-8', allow_unicode=True)
    

    @staticmethod
    def deleteTypeOfPracticeFromConfig(typeOfPractice: str):
        with open("config.yaml") as f:
            config = yaml.safe_load(f)
        
        config["typesOfPractice"] = [i for i in config["typesOfPractice"] if i["type"] != typeOfPractice]

        with open("config.yaml", "w") as f:
            yaml.dump(config ,f, encoding='UTF-8', allow_unicode=True)
