from car import Car
from car import Battery

class ElectricCar(Car):
    """ Przedstawia cechy charakterystyczne samochodu elektrycznego."""

    def __init__(self, make, model, year):
        """ Inicjalizacja atrybutów klasy nadrzędnej."""
        super().__init__(make, model, year)
        self.battery = Battery()