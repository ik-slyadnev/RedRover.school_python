# 5.1. Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов и методов
#     - как минимум один атрибут должен быть с уровнем доступа private.
#     Соответственно, для получания значений этого атрибута нужно использовать методы get и set

class Car:

    def __init__(self, make, model, year, mileage, fuel_type):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.fuel_type = fuel_type

    def get_mileage(self):
        return self.mileage

    def set_mileage(self, mileage):
        self.mileage = mileage

    def drive(self, distance):
        self.mileage += distance

    def get_fuel_type(self):
        return self.fuel_type


class ElectricCar(Car):
    def __init__(self, make, model, year, mileage):
        super().__init__(make, model, year, mileage, fuel_type='electric')

class GasolineCar(Car):
    def __init__(self, make, model, year, mileage):
        super().__init__(make, model, year, mileage, fuel_type='gasoline')


car1 = ElectricCar('Tesla', 'Model S', 2020, 0)
car2 = GasolineCar('BMW', 'X5', 2019, 10000)

print(car1.get_fuel_type())
print(car2.get_fuel_type())

print(car1.get_mileage())
car1.drive(100)
print(car1.get_mileage())

car2.set_mileage(15000)
print(car2.get_mileage())