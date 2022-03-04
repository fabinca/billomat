#remember to add your apy_key in a authentification.py file. 
#change your Billomat id and offer_id

import http.client
import json, xmltodict
from authentification import BILLOMAT_KEY

api_key = BILLOMAT_KEY
billomat_id = "sandboxedv"
offer_id = "1048814"

#getting client_id from offer_id: 
conn = http.client.HTTPSConnection(f"{billomat_id}.billomat.net")
headers = { 'Content-Type': "application/json" }
conn.request("GET", f"/api/offers/{offer_id}?api_key={api_key}")
res = conn.getresponse()
data = res.read()
data = xmltodict.parse(data)
client_id = int(data["offer"]["client_id"]["#text"])

#1. creating new invoice from offer ()
payload = f"<invoice>\n\t<client_id>{client_id}</client_id>\n\t<offer_id>{offer_id}</offer_id>\n</invoice>"
headers = { 'Content-Type': "application/xml" }
conn.request("POST", f"/api/invoices?api_key={api_key}", payload, headers)
# creates a new invoice while ignoring the details specified in offer

#2. getting items from offer
conn.request("GET", f"/api/offer_items?offer_id={offer_id}?api_key={api_key}")
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
#gives back: <error>authentication data is needed</error>
