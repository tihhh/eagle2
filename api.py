import requests, json

CAMPAIGN_API = "https://helldiverstrainingmanual.com/api/v1/war/campaign"
MAJOR_ORDER_API = "https://helldiverstrainingmanual.com/api/v1/war/major-orders"

req = requests.get(CAMPAIGN_API).json()
MajorOrder = requests.get(MAJOR_ORDER_API).json()

print(MajorOrder[0])

