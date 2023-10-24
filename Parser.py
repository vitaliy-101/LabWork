from bs4 import BeautifulSoup as bs
import requests
from Hero import Hero

class ParserFile(object):
    heroes = list()
    dotaInformation = ("Dota 2 — многопользовательская командная компьютерная игра в жанре MOBA, разработанная и "
                       "изданная корпорацией Valve. Игра является продолжением DotA — пользовательской "
                       "карты-модификации для игры Warcraft III: Reign of Chaos и дополнения к ней Warcraft III: The "
                       "Frozen Throne. Игра изображает сражение на карте особого вида; в каждом матче участвуют две "
                       "команды по пять игроков, управляющих разными «героями» — персонажами с различными наборами "
                       "способностей и характеристиками. Для победы в матче команда должна уничтожить особый объект — "
                       "«крепость», принадлежащий вражеской стороне, и защитить от уничтожения собственную "
                       "«крепость». Dota 2 работает по модели free-to-play с элементами микроплатежей.")
    def parse(self):
        URL = "https://dota2.ru/"
        req = requests.get(URL + "heroes/")
        soup = bs(req.text, "html.parser")
        allTablesUrl = soup.find_all("div", class_="base-hero__block")
        for tableUrl in allTablesUrl:
            classHeroUrl = tableUrl.find(class_="subtitle-global base-hero__subtitle")
            classHero = classHeroUrl.getText()
            allHeroesUrl = tableUrl.find_all(class_="base-hero__link-hero")
            for heroLink in allHeroesUrl:
                link = heroLink.get('href')
                textHero = heroLink.getText().lstrip().rstrip()
                hero = Hero(textHero, link, classHero)
                hero.takeDataHero()
                hero.takePhoto()
                self.heroes.append(hero)

    @property
    def getHeroes(self):
        return self.heroes

    @property
    def getDotaInformation(self):
        return self.dotaInformation
