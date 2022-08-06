import requests 

Base = "http://127.0.0.1:5000/"

data = [{"likes" : 5, "name": "How to make REST API", "views" : 76575},
        {"likes" : 97, "name": "How to play drums", "views" : 43242},
        {"likes" : 130, "name": "Jewelry", "views" : 104300}]

#send a response to this endpoint
for i in range(len(data)):
    response = requests.put(Base + "video/" + str(i), data[i])
    print(response.json())

input()
#send a response to this endpoint
response = requests.delete(Base + "video/0")
print(response)
input()  
response = requests.get(Base + "video/2")
print(response.json())