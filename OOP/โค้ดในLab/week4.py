class Agent:

    def __init__(self) :
        self._property_list = []

    def add_property(self):
        type_map = {    ("House", "Rental") : HouseRental,
                        ("House", "Purchase") : HousePurchase,
                        ("Apartment", "Rental") : ApartmentRental,
                        ("Apartment", "Purchase") : ApartmentPurchase}

        property_type = Agent.choice_property()
        purchase_type = Agent.choice_purchase()
        property_add = type_map.get((property_type, purchase_type))
        property_input = property_add.prompt_init()
        self._property_list.append(property_add(**property_input))

    def list_properties(self, show_all=False):
        if show_all:
            for property in self._property_list:
                property.display()
        else:
            id = Agent.choice_num("Enter property ID")
            for property in self._property_list:
                if property.id == int(id):
                    property.display()
                else:
                    print("Not Found")

    @staticmethod
    def choice(str_input):
        while True:
            choice_in = input(f"{str_input} \n1)Yes \n2)No \nSelect Number: ")
            if choice_in == "1" :
                return True
            elif choice_in == "2":
                return  False
            else:
                print("Try Again")
                print("="*20)

    def choice_num(int_input):
        while True:
            choice_in = input(f"{int_input} : ")
            if choice_in.isdecimal() :
                return choice_in
            else:
                print("Try Again")
                print("="*20)

    def choice_property():
        while True:
            choice_in = input("Property Type \n1)House \n2)Apartment \nSelect Number: ")
            if choice_in == "1" :
                return "House"
            elif choice_in == "2":
                return  "Apartment"
            else:
                print("Try Again")
                print("="*20)

    def choice_purchase():
        while True:
            choice_in = input("Purchase Type \n1)Rental \n2)Purchase \nSelect Number: ")
            if choice_in == "1" :
                return "Rental"
            elif choice_in == "2":
                return  "Purchase"
            else:
                print("Try Again")
                print("="*20)

class Property :
    property_id = 1

    def __init__(self, square_feet = '', num_bedroom = '', num_bathrooms = '',**kwargs):
        super().__init__(**kwargs)
        self._square_feet = square_feet
        self._num_bedroom = num_bedroom
        self._num_bathrooms = num_bathrooms
        self._property_id = Property.property_id
        Property.property_id += 1

    @property
    def id(self):
        return self._property_id

    def display(self):
        print("*"*20)
        print(f'Property ID : {self.id}')
        print(f'Square Feet : {self._square_feet} m')
        print(f'Bedroom : {self._num_bedroom} room')
        print(f'Bathrooms : {self._num_bathrooms} room')

    @staticmethod
    def prompt_init():
        dict_prop = {}
        square_feet = Agent.choice_num("Square Feet")
        num_bedroom = Agent.choice_num("Num Bedroom")
        num_bathrooms = Agent.choice_num("Num Bathrooms")

        dict_prop.update({"square_feet" : square_feet})
        dict_prop.update({"num_bedroom" : num_bedroom})
        dict_prop.update({"num_bathrooms" : num_bathrooms})
        return dict_prop
        
class House(Property):

    def __init__(self, garage = '', fenced_yard = '', **kwargs):
        super().__init__(**kwargs)
        self._garage = garage
        self._fenced_yard = fenced_yard

    def display(self):
        super().display()
        print(f'Garage : {self._garage} Uni')
        print(f'Fenced Yard : {self._fenced_yard}')
    
    @staticmethod
    def prompt_init():
        dict_house = Property.prompt_init()
        garage = Agent.choice_num("Garage")
        fenced_yard = Agent.choice("Fenced Yard")

        dict_house.update({"garage" : garage})
        dict_house.update({"fenced_yard" : fenced_yard})
        return dict_house

class Apartment(Property):

    def __init__(self, balcony = '', laundry = '', **kwargs):
        super().__init__(**kwargs)
        self._balcony = balcony
        self._laundry = laundry

    def display(self):
        super().display()
        print(f'Balcony : {self._balcony}')
        print(f'Laundry : {self._laundry}')

    
    @staticmethod
    def prompt_init():
        dict_apartment = Property.prompt_init()
        balcony = Agent.choice("Balcony")
        laundry = Agent.choice("Laundry")

        dict_apartment.update({"balcony" : balcony})
        dict_apartment.update({"laundry" : laundry})
        return dict_apartment

class Purchase:

    def __init__(self, price = '', **kwargs):
        super().__init__(**kwargs)
        self._price = price

    def display(self):
        print(f'Price : {self._price} ฿')
        print("*"*20)

    @staticmethod
    def prompt_init():
        dict_price = {}
        price = Agent.choice_num("Price")

        dict_price.update({"price" : price})
        return dict_price
        

class Rental:

    def __init__(self, furnished = '', rent = '', **kwargs):
        super().__init__(**kwargs)
        self._furnished = furnished
        self._rent = rent

    def display(self):
        print(f'Furnished : {self._furnished}')
        print(f'Rent : {self._rent} ฿')
        print("*"*20)

    @staticmethod
    def prompt_init():
        dict_rent = {}
        furnished = Agent.choice("Furnished")
        rent = Agent.choice_num("Rent")

        dict_rent.update({"furnished" : furnished})
        dict_rent.update({"rent" : rent})
        return dict_rent

class HouseRental(House, Rental) :

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def display(self):
        House.display(self)
        Rental.display(self)

    @staticmethod
    def prompt_init():
        dict_house = House.prompt_init()
        dict_rent = Rental.prompt_init()
        dict_house_rent = dict_house | dict_rent
        return dict_house_rent
        
class HousePurchase(House, Purchase) :

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def display(self):
        House.display(self)
        Purchase.display(self)

    @staticmethod
    def prompt_init():
        dict_house = House.prompt_init()
        dict_rurchase = Purchase.prompt_init()
        dict_house_rurchase = dict_house | dict_rurchase
        return dict_house_rurchase


class ApartmentRental(Apartment, Rental) :

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def display(self):
        Apartment.display(self)
        Rental.display(self)

    @staticmethod
    def prompt_init():
        dict_apart = Apartment.prompt_init()
        dict_rent = Rental.prompt_init()
        dict_apart_rent = dict_apart | dict_rent
        return dict_apart_rent

class ApartmentPurchase(Apartment, Purchase) :

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def display(self):
        Apartment.display(self)
        Purchase.display(self)

    @staticmethod
    def prompt_init():
        dict_apart = Apartment.prompt_init()
        dict_rurchase = Purchase.prompt_init()
        dict_apart_rurchase = dict_apart | dict_rurchase
        return dict_apart_rurchase

a = Agent()
a.add_property()
print("="*20)
a.add_property()
print("="*20)
a.list_properties()
