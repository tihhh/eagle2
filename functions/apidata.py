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
            self.mo = [self.api[0]['setting']['overrideBrief'],tasks]
        except:
            pass

    def getMajorOrder(self):
        return self.mo