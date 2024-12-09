import yaml

class Config:
    def __init__(self):
        with open("config.ymal") as f:
            config = yaml.safe_load(f)
        try:    
            self.directionsOfStudy = config["directionsOfStudy"]
            self.typesOfPractice = config["typesOfPractice"]
            self.nameOfOrganization = config["nameOfOrganization"]
            self.isCreateContractForOrganization = config["isCreateContractForOrganization"]
            self.directionsOfStudyParagraph = config["directionsOfStudyParagraph"]
            self.typesOfPracticeParagraph = config["typesOfPracticeParagraph"]
            self.periodOfPracticeParagraph = config["periodOfPracticeParagraph"]
        except:
            with open("config-backup.ymal", "w") as f:
                yaml.dump(config ,f, encoding='UTF-8', allow_unicode=True)

            self.directionsOfStudy = []
            self.typesOfPractice = []
            self.nameOfOrganization = "Филиал УУНиТ в г.Кумертау"
            self.isCreateContractForOrganization = True
            self.directionsOfStudyParagraph = 14
            self.typesOfPracticeParagraph = 17
            self.periodOfPracticeParagraph = 17

            config["directionsOfStudy"] = self.directionsOfStudy
            config["typesOfPractice"] = self.typesOfPractice
            config["nameOfOrganization"] = self.nameOfOrganization
            config["isCreateContractForOrganization"] = self.isCreateContractForOrganization
            config["directionsOfStudyParagraph"] = self.directionsOfStudyParagraph
            config["typesOfPracticeParagraph"] = self.typesOfPracticeParagraph
            config["periodOfPracticeParagraph"] = self.periodOfPracticeParagraph

            with open("config.ymal", "w") as f:
                yaml.dump(config ,f, encoding='UTF-8', allow_unicode=True)

    @staticmethod
    def changeIsCreateContractForOrganization ():
        with open("config.ymal") as f:
            config = yaml.safe_load(f)
        
        config["isCreateContractForOrganization"] = not config["isCreateContractForOrganization"]

        with open("config.ymal", "w") as f:
            yaml.dump(config ,f, encoding='UTF-8', allow_unicode=True)
    
    @staticmethod
    def insertNameOfOrganization(newNameOfOrganization: str):
        with open("config.ymal") as f:
            config = yaml.safe_load(f)

        config["nameOfOrganization"] = newNameOfOrganization

        with open("config.ymal", "w") as f:
            yaml.dump(config ,f, encoding='UTF-8', allow_unicode=True)

    @staticmethod
    def insertNewDirectionOfStudyToConfig(newDirectionOfStudy: str):
        with open("config.ymal") as f:
            config = yaml.safe_load(f)

        config["directionsOfStudy"].append(newDirectionOfStudy)

        with open("config.ymal", "w") as f:
            yaml.dump(config ,f, encoding='UTF-8', allow_unicode=True)

    @staticmethod
    def deleteDirectionOfStudyFromConfig(directionOfStudy: str):
        with open("config.ymal") as f:
            config = yaml.safe_load(f)

        config["directionsOfStudy"].remove(directionOfStudy)

        with open("config.ymal", "w") as f:
            yaml.dump(config ,f, encoding='UTF-8', allow_unicode=True)

    @staticmethod
    def insertNewTypeOfPracticeToConfig(newTypeOfPractice: str, durationOfPractice: str):
        with open("config.ymal") as f:
            config = yaml.safe_load(f)

        config["typesOfPractice"].append({"type": newTypeOfPractice, "duration": durationOfPractice})

        with open("config.ymal", "w") as f:
            yaml.dump(config ,f, encoding='UTF-8', allow_unicode=True)
    

    @staticmethod
    def deleteTypeOfPracticeFromConfig(typeOfPractice: str):
        with open("config.ymal") as f:
            config = yaml.safe_load(f)
        
        config["typesOfPractice"] = [i for i in config["typesOfPractice"] if i["type"] != typeOfPractice]

        with open("config.ymal", "w") as f:
            yaml.dump(config ,f, encoding='UTF-8', allow_unicode=True)
