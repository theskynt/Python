import random
import time

class Novice :

    def __init__(self, name, map) :
        self.name = name
        self.hp = 20 
        self.atk = 1
        self.exp = 0
        self.level = 1
        self.status = True
        self.x = random.randint(0, map.get_map_x())
        self.y = random.randint(0, map.get_map_y())

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


    def walk(self) :
        if self.x == 0:
            self.x += 1

        elif self.x == 10:
            self.x -= 1
        
        elif self.y == 0:
            self.y += 1

        elif self.y == 10:
            self.y -= 1

        elif  0 < self.x < 10 and 0 < self.y < 10 :
            self.x += random.randint(-1, 1)
            self.y += random.randint(-1, 1)

        return print(f"X: {self.x} Y : {self.y}")

    def sit(self):
        return print("Sitdown")

    def attack(self):
        print("Attack")
        return self.atk

    def dead(self) :
        if self.hp < 0 :
            self.status = False

class Enemy:

    def __init__(self, name, map) :
        self.name = name
        self.hp = 3 
        self.atk = 1
        self.status = True
        self.x = random.randint(0, map.get_map_x())
        self.y = random.randint(0, map.get_map_y())


    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_hp(self, new_hp):
        if isinstance(new_hp, int):
            self.hp = new_hp

    def attack(self):
        pass

    def dead(self) :
        if self.hp <= 0 :
            self.status = False

    

class Map :

    def __init__(self, x, y) :
        self.x = x
        self.y = y

    def get_map_x(self):
        return self.x

    def get_map_y(self):
        return self.y


# r = random.randint(0, 10)
testmap = Map(10, 10)

a = Novice("SKY", testmap)
b = Enemy("Zombie", testmap)


while(True):
    if a.x - b.x < 0 or a.y - b.y < 0 :
        b.set_hp(b.hp - a.attack())
        print(b.hp)
        if b.hp <= 0 :
            
            a.walk()
    else :
        a.walk()
    time.sleep(1)