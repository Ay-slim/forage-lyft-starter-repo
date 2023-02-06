from car import Car

from engines.willoughby import Willoughby
from batteries.nubbin import Nubbin


class Rorschach(Car):
    def __init__(self, last_service_mileage, current_mileage, last_service_date):
        rorschach_engine = Willoughby(last_service_mileage, current_mileage)
        rorschach_battery = Nubbin(last_service_date)
        super().__init__(rorschach_engine, rorschach_battery)
        self.engine = rorschach_engine
        self.battery = rorschach_battery

    def needs_servicing(self):
        return super().needs_servicing()