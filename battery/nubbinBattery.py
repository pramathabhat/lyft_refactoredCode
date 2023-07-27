from battery.battery import Battery
from utils import add_years

class NubbinBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date 
        self.last_service_date = last_service_date
        self.years = 4

    def needs_service(self):
        battery_service_date = add_years(self.last_service_date, self.years); 
        return battery_service_date < self.current_date;