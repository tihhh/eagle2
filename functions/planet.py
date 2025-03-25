import os
from functions.func import *



class PlanetHandler():
    def __init__(self):
        self.biomes = loadJson(os.path.join(os.path.dirname(__file__), '../data', 'biomes.json'))
        self.ownerLogo = loadJson(os.path.join(os.path.dirname(__file__), '../data', 'owners.json'))

    def getPlanet(self, planets, planet):
        "If string, search for name, if int, search by id"
        for i in planets:
            if i['name'].lower() == planet.lower():
                return i
    
    def returnBiome(self, planet):
        #returns [biome_type, biome desc, biome_image] (string)
        biomeList = loadJson(os.path.join(os.path.dirname(__file__), '../data', 'biomes.json'))
        planetList = loadJson(os.path.join(os.path.dirname(__file__), '../data', 'planets.json'))
        
        biome = planetList[str(planet['planetIndex'])]['biome']
        biomeDesc = biomeList[str(biome)]['description']
        biomeImage = biomeList[str(biome)]['image_link']
        bi = [biome, biomeDesc, biomeImage]
        return bi
    
    def returnOwnerLogo(self, planet):
        return self.ownerLogo[str(planet['faction'])]

    def getDefense(self, planet):
        if planet['expireDateTime'] == None:
            return False
        else:
            return time_until_target(planet['expireDateTime'])