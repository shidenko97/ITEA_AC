import json
from collections import namedtuple

Car = namedtuple("Tesla", ["color", "mileage"])
# same as:
# Car = namedtuple('Car' , 'color mileage')
my_car = Car("red", 3812.4)
color, mileage = my_car

tuple(my_car)

# my_car.color = 'blue'
my_car._replace(color="blue")

my_car._asdict()

json.dumps(my_car._asdict())
