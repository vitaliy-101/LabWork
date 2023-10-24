from bs4 import BeautifulSoup as bs
import requests
from Abilities import Abilities

class Hero(object):
    information = ""
    classHero = ""
    abilities = 0
    def __init__(self, name, heroUrl, classHero):
        self.name = name
        self.heroUrl = "https://dota2.ru/" + heroUrl
        self.classHero = classHero.lstrip().rstrip()

    @property
    def getInformation(self):
        return self.information

    @property
    def getClassHero(self):
        return self.classHero

    @property
    def getNameHero(self):
        return self.name

    @property
    def getAbilitiesHero(self):
        return self.abilities
    def takeDataHero(self):
        self.createInformation()
        self.abilities = Abilities(self.heroUrl)
        self.abilities.createAbilitiesList()


    def createInformation(self):
        req = requests.get(self.heroUrl)
        soup = bs(req.text, "html.parser")
        self.information = soup.find(class_="base-hero-hero__descr-text").getText().lstrip().rstrip()

