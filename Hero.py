from bs4 import BeautifulSoup as bs
import requests
class Hero(object):
    information = ""
    classHero = ""
    def __init__(self, name, heroUrl, classHero):
        self.name = name
        self.heroUrl = "https://dota2.ru/" + heroUrl
        self.classHero = classHero.lstrip().rstrip()


    def takeDataHero(self):
        self.createInformation()


    def createInformation(self):
        req = requests.get(self.heroUrl)
        soup = bs(req.text, "html.parser")
        self.information = soup.find(class_="base-hero-hero__descr-text").getText().lstrip().rstrip()

