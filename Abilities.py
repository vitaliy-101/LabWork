from bs4 import BeautifulSoup as bs
import requests
class Abilities(object):


    def __init__(self, abilitiesUrl):
        self.abilitiesUrl = abilitiesUrl

    @property
    def getAbilitiesList(self):
        return self.abilitiesList


    def createAbilitiesList(self):
        req = requests.get(self.abilitiesUrl)
        soup = bs(req.text, "html.parser")
        allAbilities = soup.find("div", class_="base-hero-hero__descr-attr")
        textHeroAbilities = self.createTextHeroAbilities(allAbilities)
        abilitiesList = {
            "Cила": 0,
            "Ловкость": 0,
            "Интеллект": 0,
            "Урон": 0,
            "Защита": 0,
            "Скорость": 0
        }
        ind = 0
        for key in abilitiesList:
            abilitiesList[key] = textHeroAbilities[ind].replace(' ', '')
            ind += 1
        self.abilitiesList = abilitiesList


    def createTextHeroAbilities(self, allAbilities):
        textHeroAbilities = allAbilities.getText().lstrip().rstrip().replace('\n', ' ').split('   ')
        return textHeroAbilities




