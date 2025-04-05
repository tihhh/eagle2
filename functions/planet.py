import os
from functions.func import *



class PlanetHandler():
    def __init__(self):
        self.biomes = loadJson(os.path.join(os.path.dirname(__file__), '../data', 'biomes.json'))
        self.ownerLogo = loadJson(os.path.join(os.path.dirname(__file__), '../data', 'owners.json'))
        self.fullPlanetList = loadJson(os.path.join(os.path.dirname(__file__), '../data', 'planets.json'))
        self.biomeList = loadJson(os.path.join(os.path.dirname(__file__), '../data', 'biomes.json'))
        self.planetList = loadJson(os.path.join(os.path.dirname(__file__), '../data', 'planets.json'))
        self.planetEffects = loadJson(os.path.join(os.path.dirname(__file__), '../data', 'planetEffects.json'))

    def getPlanet(self, planets, planet):
        "If string, search for name, if int, search by id"
        for i in planets:
            if i['name'].lower() == planet.lower():
                return i
    
    def returnBiome(self, planet):
        #returns [biome_type, biome desc, biome_image] (string)

        
        biome = self.planetList[str(planet['planetIndex'])]['biome']
        biomeDesc = self.biomeList[str(biome)]['description']
        biomeImage = self.biomeList[str(biome)]['image_link']
        bi = [biome, biomeDesc, biomeImage]
        return bi
    
    def returnId(self, name):
        for planet_id, planet_data in self.planetList.items():
            if planet_data.get("name").lower() == name.lower():
                return int(planet_id)
            
        return None

    def returnPlanetDetailed(self, planetID):
        planet = self.fullPlanetList[str(planetID)]
        filtered_a = [item for item in planet['weather_effects'] if item != "normal_temp"]
        result = list(set(filtered_a + planet['environmentals']))
        result_string = ', '.join(result)
        return [planetID, #0
                planet['name'], #1
                planet['sector'], #2
                planet['biome'], #3
                result_string] #4
    
    def returnBiomeInfoFromBiome(self, biome):
        return [self.biomeList[str(biome)]['description'], self.biomeList[str(biome)]['image_link']]
    
    def returnGalacticEffects(self, status, planetId):
        effectsID = []
        for i in status["planetActiveEffects"]:
            if i["index"] == planetId:
                effectsID.append(i["galacticEffectId"])
        galacticEffects = {}
        for i in effectsID:
            galacticEffects.update({self.planetEffects[str(i)]['name'] : self.planetEffects[str(i)]['description']})
        
        return galacticEffects

    
    def returnOwnerLogo(self, planet):
        "planet can be either faction id or planet (yes i know this is shit)"
        return self.ownerLogo[str(planet['faction'])]
    
    def returnOwnerLogoByID(self, owner_id):
        return self.ownerLogo[str(owner_id)]

    def getDefense(self, planet):
        if planet['expireDateTime'] == None:
            return False
        else:
            return time_until_target(planet['expireDateTime'])
        
    def getPlanetStatus(self, planetStatus, planet_id):
        for i in planetStatus['planetStatus']:
            if (i["index"] == planet_id):
                return i
        return None