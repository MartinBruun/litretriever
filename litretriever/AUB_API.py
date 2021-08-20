import requests
import json

response = requests.get("https://kbdk-aub.primo.exlibrisgroup.com")

# Test connection
if response.status_code == 200:
    print("A.Okay")
else:
    print("no no no")

print(response.content)