from random import randint, choice
from .attachments import list, listEng

class generator:
    def __init__(self, lang : str) -> str:

        if lang == 'RU':
            self.list = list
            self.gender = choice(['Мужской', 'Женский'])
        else:
            self.list = listEng
            self.gender = choice(['Male', 'Female'])

        self.surname = choice(self.list['Surname'])
        self.race = choice(self.list['raceList'])

        if self.gender == 'Мужской' or 'Male': self.name = choice(self.list['Gender']['Male']['Name'])
        else: self.name = choice(self.list['gender']['Female']['Name'])

        if self.race == self.list['raceList'][0]: self.age = randint(1, 100)
        else: self.age = randint(1, 1000)

        self.eyeColor = choice(self.list['eyeColor'])
        self.hairColor = choice(self.list['hairColor'])
        self.sociability = choice(self.list['sociability'])