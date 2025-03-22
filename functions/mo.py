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
    #['Defend against the Automaton offensive, led by the newly-built Incineration Corps, or collect enough E-710 to activate the Penrose Energy Siphon and reduce Dark Energy Accumulation.', 
    # [{'Task': 12, '3': 8, '1': 3, '11': 0, '12': 0}, {'Task': 3, '1': 2, '2': 1, '3': 1250000000, '4': 0, '6': 0, '5': 0, '8': 0, '9': 0, '11': 0, '12': 0}], 
    # 137920, 
    # [2, 588353971], 
    # [[1, 55]]]
    def __init__(self):
        pass
    
    def returnBrief(self, data):
        return data[0]
    
    def returnSeconds(self, data):
        return data[2]

    
    def formatTasks(self, data):
    #data format: ["brief", {'Task': 12, 3: 8, 1: 3, 11: 0, 12: 0}, ]
        print(str(data[0]))
        for order in data[1]:
            if (order['Task'] == 12):
                if (order['12'] == 0):
                    print("Defend " + str(order['3']) + " attacks from the " + str(faction[str(order['1'])]))
                else:
                    pass
            elif(order['Task'] == 3):
                #{'Task': 3, '1': 2, '2': 1, '3': 1250000000, '4': 0, '6': 0, '5': 0, '8': 0, '9': 0, '11': 0, '12': 0}]]
                if(order['4'] == 0):
                    print("Eradicate " + f"{order['3']:,}" + " " + str(faction[str(order['1'])]))
                else:
                    print("Eradicate " + f"{order['3']:,}" + " " + "SOMETHING")
        
            else:
                print("UNKNOWN TASK")
    