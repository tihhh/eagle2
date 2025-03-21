import requests

API = "https://api.diveharder.com/v1/major_order"

"""
    "2": "Extract",
    "3": "Eradicate",
	"11": "Liberation",
	"12": "Defense",
	"13": "Control",
	"15": "Expand"
"""

task = {'2': "Extract", 
        '3': "Eradicate", 
        '11': "Liberate", 
        "12": "Defense",
        "13": "Control"}

class MajorOrder:
    def __init__(self):
        self.api = requests.get(API).json()


    def returnMoBrief(self):
        try:
            return self.api[0]['setting']['overrideBrief']
        except:
            return None
    
    def returnTasks(self):
        #Returns dictionary of value
        try:
            for i in self.api[0]['setting']['tasks']:
                return [task[i['type']], ]
        except:
            return None