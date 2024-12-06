import yaml

class Config:
    def __init__(self):
        with open("config.ymal") as f:
            config = yaml.safe_load(f)
        self.directionsOfStudy = config["directionsOfStudy"]
        self.typesOfPractice = config["typesOfPractice"]

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
