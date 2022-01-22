#To get covid vaccination slots by using pincode and date 

import requests
import json
from json2html import *

#Function 1 - To process data received from api to json format
def processapidatato_json(data):
    text = json.dumps(data, sort_keys=True, indent=4)
    return text

#Paramters to be passed to the API [pincode + date]
parameters = {
    "pincode": 560048,
    "date": "22-01-2022"
}

#Get information from API to get vaccination slots based on pincode and date
response = requests.get(
    "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin", params=parameters)
slot_information = processapidatato_json(response.json())
jsontohtml = json2html.convert(slot_information)

#HTML Format - Head + Body
htmlstart = """
<html><head><title>>Covd-19 Vaccination Slots Tracker</title><style>
table {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

<Please give in pincode>
Pincode:
<br> <br>

Date:
<input>
<br> <br>

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

#HTML Format - End
htmlend = """
</body></html>
"""

# Combine html code and json formatted data received from API
contenttowrite = htmlstart + jsontohtml + htmlend

#Write the complete content to file
writetofile = open("covid19_vaccine_available_slots.html", "w")
writetofile.write(contenttowrite)
writetofile.close()
writetofile.close()

print ("SUCCESS: Data retrieved from API and written to HTML file successfully!")
