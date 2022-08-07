import requests 

Base = "http://127.0.0.1:5000/"


response = requests.patch(Base + "video/2", { "views": 99, "likes": 1000})
print(response.json())