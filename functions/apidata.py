import requests

class APIData:
    def __init__(self):
        self.moAPI = requests.get("https://helldiverstrainingmanual.com/api/v1/war/major-orders").json()
        self.mo = None
        self.planets = requests.get("https://helldiverstrainingmanual.com/api/v1/war/campaign").json()
        self.planetStatus = requests.get("https://helldiverstrainingmanual.com/api/v1/war/status").json()
        self.news = requests.get("https://api.diveharder.com/v1/news_feed").json()
        self.callMajorOrderAPI()

    def callMajorOrderAPI(self):
            
        #Major order
        try:
            tasks = []
            for item in self.moAPI[0]['setting']['tasks']:
                taskDict = {}
                taskDict.update({"Task" : item['type']})
                values = []
                i=0
                for v in item['values']:
                    taskDict.update({str(item['valueTypes'][i]) : v})
                    i +=1

                tasks.append(taskDict)
            rewards = []
            for reward in self.moAPI[0]['setting']['rewards']:
                #return ["type", "amount"]
                rewards.append([reward['type'], reward['amount']])
                
            self.mo = [self.moAPI[0]['setting']['overrideBrief'], #MO Brief
                    tasks, #Tasks
                    self.moAPI[0]['expiresIn'], #Expire (seconds)
                    self.moAPI[0]['progress'], #Progress 
                    rewards #Rewards for winning Major Order
                    ]
        except:
            print("Failed to fetch")

    def getPlanets(self):
        return self.planets
    
    def getPlanetById(self, id):
        return self.planets[str(id)]

    

    def getMajorOrder(self):
        return self.mo