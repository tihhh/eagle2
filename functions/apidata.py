import requests

API = "https://api.diveharder.com/v1/major_order"
class APIData:
    def __init__(self):
        self.api = requests.get(API).json()
        self.mo = None

    def callMajorOrderAPI(self):
        #Major order
        try:
            tasks = []
            for item in self.api[0]['setting']['tasks']:
                taskDict = {}
                taskDict.update({"Task" : item['type']})
                values = []
                i=0
                for v in item['values']:
                    taskDict.update({str(item['valueTypes'][i]) : v})
                    i +=1

                tasks.append(taskDict)
            rewards = []
            for reward in self.api[0]['setting']['rewards']:
                #return ["type", "amount"]
                rewards.append([reward['type'], reward['amount']])
                
            self.mo = [self.api[0]['setting']['overrideBrief'], #MO Brief
                       tasks, #Tasks
                       self.api[0]['expiresIn'], #Expire (seconds)
                       self.api[0]['progress'], #Progress 
                       rewards #Rewards for winning Major Order
                       ]
        except:
            print("Failed to fetch")

    def getMajorOrder(self):
        return self.mo