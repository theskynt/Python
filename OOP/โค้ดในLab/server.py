# Importing the FastApi class
from fastapi import FastAPI
import json

# Creating an app object
app = FastAPI()

class Admin:

    def __init__(self):
        self.__menu = []

    def add_menu(self, new_menu) :
        with open('test_2.json') as fp:
            self.__menu = json.load(fp)

        self.__menu.append(new_menu)

        with open('test_2.json', 'w') as json_file:
            json.dump(self.__menu, json_file, 
                        indent=4,  
                        separators=(',',': '))

        return id

    def get_menu(self):
        return self.__menu

    def modify_menu(self, id, fix_menu):
        for menu in self.__menu:
            if (int(menu["ID"])) == id:
                menu["Name"] = fix_menu["Name"]
                menu["Type"] = fix_menu["Type"]
                menu["Water"] = fix_menu["Water"]
                menu["Ice"] = fix_menu["Ice"]
                menu["Milk"] = fix_menu["Milk"]
                menu["Milk_Foam"] = fix_menu["Milk_Foam"]
                menu["Price"] = fix_menu["Price"]
                return {
                    "menulist": f"Menu ID : {id} updated"
                }
        return {
            "menulist": f"ID {id} is not found!"
        }

    def delete_menu(self, id):
        for menu in self.__menu:
            if int(menu["ID"]) == id:
                self.__menu.remove(menu)
                return {
                    "menulist": f"Menu ID : {id} delete"
                }
        return {
            "menulist": f"ID {id} is not found!"
        }


my_admin = Admin()

@app.get("/", tags=['root'])
async def root() -> dict:
    return {"Hello": "World"}

# Post -- > Create Menu
@app.post("/menu", tags=['Menu'])
async def add_menu(menu: dict) -> dict:
    id = my_admin.add_menu(menu)
    todo = "A menu "+str(id)+" is added!"
    return {
        "data": todo
    }

# GET -- > Read Menu
@app.get("/menu", tags=['Menu'])
async def get_menu() -> dict:
    return {"Menu": my_admin.get_menu()}

# PUT  -- > Update Todo
@app.put("/menu/{id}", tags=['Menu'])
async def update_menu(id: int, fix_menu: dict) -> dict:
    return my_admin.modify_menu(id, fix_menu)

# DELETE --> Delete Todo
@app.delete("/menu/{id}", tags=['Menu'])
async def delete_menu(id: int) -> dict:
    return my_admin.delete_menu(id)
