#!/usr/bin/env python


class RaceCar:

    # init function inside the class
    def __init__(self, color, fuel_remaining, laps=0, **kwargs):
        self.color = color
        self.fuel_remaining = fuel_remaining
        self.laps = laps

        for key, value in kwargs.items():
            setattr(self, key, value)

    # run_lap method
    def run_lap(self, lenght):
        self.laps += 1
        self.fuel_remaining =  self.fuel_remaining - ((lenght) * 0.125)
        return  self.fuel_remaining

object = RaceCar("Red", 15)
print (object.color)
print (object.fuel_remaining)
print (object.run_lap(10))
print (object.laps)

