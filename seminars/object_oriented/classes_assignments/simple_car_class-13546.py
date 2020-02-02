"""
Link: http://lifemichael.com/moodle/mod/assign/view.php?id=13546

Develop a separated module the includes the definition for the Car class.
The variables each Car object should have are 'brand', 'model', 'id' and 'year'.

Develop a simple separated module (that uses the Car module)
that includes simple code for creating a Car object that represents your car,
and write the required code for printing its details to the screen.
"""
from seminars.object_oriented.classes_assignments.simple_car_class_13546.module import CarData


class Car(CarData):
    def __init__(self, cid, brand, model, year):
        super().__init__(cid, brand, model, year)
        self.__cid = cid
        self.__brand = brand
        self.__model = model
        self.__year = year

    @property
    def car_id(self):
        return self.__cid

    @car_id.setter
    def car_id(self, data):
        self.__cid = data

    @property
    def car_brand(self):
        return self.__brand

    @property
    def car_model(self):
        return self.__model

    @property
    def car_year(self):
        return self.__year

    @car_year.setter
    def car_year(self, year):
        self.__year = year

    def __str__(self):
        return "Car ID: " + str(self.car_id) + \
               "\nCar brand: " + str(self.car_brand) + \
               "\nCar model: " + str(self.car_model) + \
               "\nCar year: " + str(self.car_year)


# List of the cars
ob = [
    Car(242142, "Honda", "Civic", 2003),
    Car(242143, "Suzuki", "Vitara", 2000),
    Car(842143, "Suzuki", "Baleno", 1999),
    Car(642143, "Hundai", "i10", 2020),
    Car(642143, "Hundai", "oldie", 1920),
    Car(642143, "Hundai", "i10", 1989)
]
# Print the list of the cars one after another
# for cars in ob:
for cars in ob:
    if cars.car_year >= 2000:
        print("-------New car---------")
        print(cars)
    else:
        print("-------Old car---------")
        print(cars)
