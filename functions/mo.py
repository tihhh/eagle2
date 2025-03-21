import requests

API = "https://api.diveharder.com/v1/major_order"

"""
	"1": "Humans",
	"2": "Terminids",
	"3": "Automaton",
	"4": "Illuminate"
"""
""" 
    "2": "Extract",
    "3": "Eradicate",
	"11": "Liberation",
	"12": "Defense",
	"13": "Control",
	"15": "Expand"
"""
"""
	"1": "race",
	"2": "unknown",
	"3": "goal",
	"4": "unit_id",
	"5": "item_id",
	"11": "liberate",
	"12": "planet_index"
"""

task = {'2': "Extract", 
        '3': "Eradicate", 
        '11': "Liberate", 
        "12": "Defense",
        "13": "Control"}
faction = {
    "1": "Humans",
	"2": "Terminids",
	"3": "Automatons",
	"4": "Illuminates"
}

class MajorOrderHandler():
    def __init__(self):
        pass

    def formatOrder(self, mo):
    #data format: ["brief", {'Task': 12, 3: 8, 1: 3, 11: 0, 12: 0}]
        print(str(mo[0]))
        for order in mo[1]:
            if (order['Task'] == 12):
                if (order['12'] == 0):
                    print("Defend " + str(order['3']) + " attacks from the " + str(faction[str(order['1'])]))
                else:
                    pass
            elif(order['Task'] == 3):
                print("Eradicate " + str(order['3']) + " " + str(faction[str(order['1'])]))
        
            else:
                print("TASK UNKNOWN (Bot not updated)")