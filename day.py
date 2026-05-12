class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def full_name(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):
        return "petrol or disel"
    
class ElectricCar(Car):
    def __init__(self, brand, model):
        super().__init__(brand, model)
    
    def fuel_type(self):
        return "electric charge"


my_electri=ElectricCar("tesla","modelS")
print(my_electri.fuel_type())

safari=Car("tata","safari")
print(safari.fuel_type())

print(isinstance(my_electri,Car))
print(isinstance(safari,Car))
# print(my_electri.brand)
# print(my_electri.model)
# print(my_electri.full_name())

# my_car=Car("tata","safari")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# my_new_car=Car("hundai","i10")
# print("company name is:",my_new_car.brand)
# print("Brand name is:",my_new_car.model)

        