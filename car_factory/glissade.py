from car import Car

from engines.willoughby import Willoughby
from batteries.spindler import Splinder

class Glissade(Car):
    def __init__(self, last_service_mileage, current_mileage, last_service_date):
        glissade_engine = Willoughby(last_service_mileage, current_mileage)
        glissade_battery = Splinder(last_service_date)
        super().__init__(glissade_engine, glissade_battery)
        self.engine = glissade_engine
        self.battery = glissade_battery
    
    def needs_servicing(self):
        return super().needs_servicing()
