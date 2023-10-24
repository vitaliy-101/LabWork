from bs4 import BeautifulSoup as bs
import requests
class Abilities(object):
    abilitiesList = {
        "Cила": 0,
        "Ловкость": 0,
        "Интеллект": 0,
        "Урон": 0,
        "Защита": 0,
        "Скорость": 0
    }

    def __init__(self, abilitiesUrl):
        self.abilitiesUrl = abilitiesUrl

    @property
    def getAbilitiesList(self):
        return self.abilitiesList

    def createAbilitiesList(self):
        req = requests.get(self.abilitiesUrl)
        soup = bs(req.text, "html.parser")
        allAbilities = soup.find_all("div", class_="base-hero-hero__descr-attr")
        textHeroAbilities = self.createTextHeroAbilities(allAbilities)
        ind = 0
        for key in self.abilitiesList:
            self.abilitiesList[key] = textHeroAbilities[ind].replace(' ', '')
            ind += 1

    @staticmethod
    def createTextHeroAbilities(allAbilities):
        textHeroAbilities = ''
        for ability in allAbilities:
            textHeroAbilities += ability.getText().lstrip().rstrip().replace('\n', ' ')
        return textHeroAbilities.split('   ')




