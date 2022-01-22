#To get covid vaccination slots by pincode and date
import requests
import json
def processapidatato_json(data):
    text = json.dumps(data, sort_keys=True, indent=4)
    print(text)
 
parameters = {
    "pincode": 411033,
    "date": "22-01-2022"
}
response = requests.get(
    "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin", params=parameters)

processapidatato_json(response.json())

