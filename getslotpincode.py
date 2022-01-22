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
#Find slots for pin-code
response = requests.get(
    "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin", params=parameters)

slot_information = processapidatato_json(response.json())

jsontohtml = json2html.convert(slot_information)

htmlstart = """
<html><head><title>>Covd-19 Vaccination Slots Tracker</title><style>
table {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #ddd;
  padding: 8px;
}

tr:nth-child(even){background-color: #66b2b2;}

tr:hover {background-color: #ddd;}

th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #66b2b2;
  color: white;
}
</style></head><body>
<h1> COVID-19 VACCINATION SLOTS FINDER </h1>
"""

htmlend = """
</body></html>
"""

contenttowrite = htmlstart + jsontohtml + htmlend

writetofile = open("slot_info.html", "w")
writetofile.write(contenttowrite)
writetofile.close()
writetofile.close()

print ("SUCCESS: Data retrieved from API and written to HTML file successfully!")




    

