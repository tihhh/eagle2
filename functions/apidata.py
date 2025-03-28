import requests

MO_API = "https://api.diveharder.com/v1/major_order"
class APIData:
    def __init__(self):
        with requests.get(MO_API) as f:
            if f.status_code == 200:
                self.moAPI = f
            else:
                self.moAPI = []
        self.mo = None
        self.planets = requests.get("https://helldiverstrainingmanual.com/api/v1/war/campaign").json()

    def callMajorOrderAPI(self):
            
        #Major order
        if (self.moAPI != []):
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
        else:
            return None

    def getPlanets(self):
        return self.planets

    

    def getMajorOrder(self):
        return self.mo