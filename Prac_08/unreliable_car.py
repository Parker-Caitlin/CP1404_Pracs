from car import Car
from random import randrange

class UnreliableCar(Car):


    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability


    def drive(self, distance):
        distance_driven = 0
        if randrange(0, 100, 1) < self.reliability:
            distance_driven = super().drive(distance)
        return distance_driven


