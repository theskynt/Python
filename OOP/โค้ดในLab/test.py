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
        square_feet = 1
        num_bedroom = 2
        num_bathrooms = 3

        dict_prop.update({"square_feet" : square_feet})
        dict_prop.update({"num_bedroom" : num_bedroom})
        dict_prop.update({"num_bathrooms" : num_bathrooms})
        return dict_prop

s = Property()

print(s.prompt_init())
s.display()