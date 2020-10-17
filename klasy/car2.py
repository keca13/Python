class Car():
    def __init__(self, make, model, year):
        """Inicjalizacja atrybutów opisujących samochód"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_describe_name(self):
        """Zwrot elegancko sformatowanego opisu samochodu"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Wyswietla informacje o przebiegu samochodu"""
        print(f'Ten samochod ma przejechane {self.odometer_reading } km')
        
my_new_car = Car('audi','A4','2019')
print(my_new_car.get_describe_name())
my_new_car.read_odometer()