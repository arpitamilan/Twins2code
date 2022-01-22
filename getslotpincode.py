#To get covid vaccination slots by pincode and date
import requests
import json

def processapidatato_json(data):
    text = json.dumps(data, sort_keys=True, indent=4)
    print(text)

togetdata = {
    "pincode": 411033,
    "date": "23-01-2022"
}

apidata = requests.get(
    "https://cdn-api.co-vin.in/api/v2​/appointment​/sessions​/public​/findByPin",params=togetdata)

processapidatato_json(apidata.json())

