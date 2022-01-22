# to get covid vaccine slots through district name

import requests
import json

togetdata= {
    "district": "Belagavi",
    "date": "22-01-2022"
}

def processapidatato_json(data):
    text = json.dumps(data, sort_keys=True, indent=4)
    print(text)

apidata = requests.get(
    "https://cdn-api.co-vin.in/api/v2/admin/location/districts/16")

processapidatato_json(apidata.json())

