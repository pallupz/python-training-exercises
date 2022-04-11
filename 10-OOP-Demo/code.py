

class Vehicle:
    def __init__(self, color, num_tyres, mileage, tank_capacity):
        self.color = color
        self.num_tyres = num_tyres
        self.mileage = mileage
        self.tank_capacity = tank_capacity

        self.range = mileage * tank_capacity

    @property
    def range_v2(self):
        return self.mileage * self.tank_capacity


car = Vehicle('black', 4, 15, 20)

print(car.color)
print(car.mileage)
print(car.range)
print(car.range_v2)

car.mileage = 20
print(car.mileage)
print(car.range)
print(car.range_v2)
