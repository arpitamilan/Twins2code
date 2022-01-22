#To get covid vaccination slots by pincode and date
import requests
import json
from json2html import *

def processapidatato_json(data):
    text = json.dumps(data, sort_keys=True, indent=4)
    #print(text)
    return text
 
parameters = {
    "pincode": 411033,
    "date": "22-01-2022"
}
# find slots for pin code 
response = requests.get(
    "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin", params=parameters)
slot_information = processapidatato_json(response.json())

print(slot_information)

htmlout = jason2html.converter(slot_information)

print(htmlout)

file1 = open("slot_info.html", "w")

file1.write(htmlout)



    

