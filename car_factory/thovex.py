from car import Car

from engines.capulet import Capulet
from batteries.nubbin import Nubbin


class Thovex(Car):
    def __init__(self, last_service_mileage, current_mileage, last_service_date):
        thovex_engine = Capulet(last_service_mileage, current_mileage)
        thovex_battery = Nubbin(last_service_date)
        super().__init__(thovex_engine, thovex_battery)
        self.engine = thovex_engine
        self.battery = thovex_battery

    def needs_servicing(self):
        return super().needs_servicing()
