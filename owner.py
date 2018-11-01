# import car class here
from car import Car
# even though you're giving the car object an attribute labeled owner
# you want to import the car class here to call the car object with the owner attribute
# you define car objects elsewhere, not in the blueprint/class object, that's why
# you're able to import from car class here. car and owner classes are not calling each other

class Owner:
    all = []
    def __init__(self, name, age):
        self._name = name
        self._age = age
        Owner.all.append(self)

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name = name

    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,age):
        self._age = age

    def find_my_cars(self):
        list_cars =  list(filter(lambda car: vars(car)['_owner'] == self, Car._all))
        return list(map(lambda car: vars(car)['_make'] + ' ' + vars(car)['_model'], list_cars))
