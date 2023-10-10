import requests
import json


# menu = {"ID": 1, "Name" : "GreenTea" ,"Type" : "Tea" ,"Water" : 100 ,"Ice" : 20 ,"Milk" : 30 ,"Milk_Foam" : 10 ,"Price" : 30}
# r = requests.post("http://127.0.0.1:8000/menu",data=json.dumps(menu))
# print(r.json())

menu = {"ID": 4, "Name" : "Latte2" ,"Type" : "Coffee" ,"Water" : 100 ,"Ice" : 20 ,"Milk" : 30 ,"Milk_Foam" : 10 ,"Price" : 30}
r = requests.post("http://127.0.0.1:8000/menu",data=json.dumps(menu))
print(r.json())

menu = {"ID": 1, "Name" : "coco" ,"Type" : "Coffee" ,"Water" : 100 ,"Ice" : 20 ,"Milk" : 30 ,"Milk_Foam" : 10 ,"Price" : 30}
r = requests.put("http://127.0.0.1:8000/menu/1",data=json.dumps(menu))
print(r.json())


r = requests.get("http://127.0.0.1:8000/menu")
print(r.json())
# data = r.json()
# print(data['Menu'][1])

