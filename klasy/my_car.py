from car import Car 
from electric_car import ElectricCar
from car import Battery

my_beetle = Car('volksvagen', 'beetle', 2009)
print(my_beetle.get_descripting_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descripting_name())
print(my_tesla.Battery())
#my_battery = ElectricCar.Battery()
#print(my_battery.describe_battery())
#print(my_battery.battery_size)