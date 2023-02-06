from car import Car

from engines.capulet import Capulet
from batteries.spindler import Splinder


class Calliope(Car):
    def __init__(self, last_service_mileage, current_mileage, last_service_date):
        calliope_engine = Capulet(last_service_mileage, current_mileage)
        calliope_battery = Splinder(last_service_date)
        super().__init__(calliope_engine, calliope_battery)
        self.engine = calliope_engine
        self.battery = calliope_battery

    def needs_servicing(self):
        return super().needs_servicing()


