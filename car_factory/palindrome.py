from car import Car

from engines.sternman import Sternman
from batteries.spindler import Splinder


class Palindrome(Car):
    def __init__(self, warning_light_is_on, last_service_date):
        palindrome_engine = Sternman(warning_light_is_on)
        palindrome_battery = Splinder(last_service_date)
        super().__init__(palindrome_engine, palindrome_battery)
        self.engine = palindrome_engine
        self.battery = palindrome_battery

    def needs_servicing(self):
        return super().needs_servicing()
