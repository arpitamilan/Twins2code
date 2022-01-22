# to get district code

import requests
import json

def processapidatato_json(data):
    text = json.dumps(data, sort_keys=True, indent=4)
    print(text)

apidata = requests.get(
    "https://cdn-api.co-vin.in/api/v2/admin/location/districts/36")

processapidatato_json(apidata.json())

