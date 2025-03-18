import requests
import tqdm
from func import progressBar

CAMPAIGN_API = "https://helldiverstrainingmanual.com/api/v1/war/campaign"
MAJOR_ORDER_API = "https://helldiverstrainingmanual.com/api/v1/war/major-orders"
#Get a better API with more info next time

req = requests.get(CAMPAIGN_API).json()

MajorOrder = requests.get(MAJOR_ORDER_API).json()

print(MajorOrder[0])

def getPlanet(name):
    for i in req:
        if i['name'].lower() == name.lower():
            return i

    return None

def sendPlanetInfo(Planet):
    print("Planet: " + Planet['name'])
    print("Faction: " + Planet['faction'])
    print("Percentage: " + progressBar(Planet['percentage']))

def getMajorOrder():
    print("MAJOR ORDER")
    print(MajorOrder[0]['setting']['overrideBrief'])


r = getPlanet("Vog-Sojoth")
sendPlanetInfo(r)


