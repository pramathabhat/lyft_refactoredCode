from datetime import datetime
from carFactory import CarFactory

current_date = datetime.now()
last_service_date = datetime(2019, 11, 26)
current_mileage = 50000
last_service_mileage = 48000

# Creating an object of CarFactory
factory = CarFactory()

# Calling the create_calliope method
created_car = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
print(created_car)
print(created_car.battery.needs_service())
print(created_car.engine.needs_service())
