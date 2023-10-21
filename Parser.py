from bs4 import BeautifulSoup as bs
import requests
from Hero import Hero

class ParserFile(object):
    heroes = list()
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
                self.heroes.append(hero)