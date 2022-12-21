import requests
import json

dataToBeSent={}
dataToBeSent["name"]="Avirup Basu"
dataToBeSent["githubUserName"]="avirup171"

postURL="http://localhost:8081/data"

jsonData=json.dumps(dataToBeSent)
headers =  {"Content-Type":"application/json"}
response = requests.post(postURL,jsonData,headers=headers)
print(response.json())