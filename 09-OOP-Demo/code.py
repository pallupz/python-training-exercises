# Exercise Name:
# 	09-OOP-Demo
# Description:
# 	Create a class and demonstrate how @property decorator is used

class Vehicle:
    def __init__(self, color, num_tyres, mileage, fuel_volume):
        self.color = color
        self.num_tyres = num_tyres
        self.mileage = mileage
        self.fuel_volume = fuel_volume

        self.range = mileage * fuel_volume

    def drive(self, distance):
        fuel_used = distance / self.mileage
        self.fuel_volume -= fuel_used

    @property
    def range_v2(self):
        return self.mileage * self.fuel_volume


car = Vehicle('black', 4, 15, 20)

print('----------------')
print(car.color)
print(car.mileage)
print(car.range)
print(car.range_v2)

print('----------------')
car.mileage = 20
print(car.mileage)
print(car.range)
print(car.range_v2)

print('----------------')
print(car.fuel_volume)
print(car.range_v2)

print('----------------')
car.drive(20)
print(car.fuel_volume)
print(car.range_v2)

