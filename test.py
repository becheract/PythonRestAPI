import requests 

Base = "http://127.0.0.1:5000/"

#send a response to this endpoint
reponse = requests.get(Base + "helloworld")

print(reponse.json())