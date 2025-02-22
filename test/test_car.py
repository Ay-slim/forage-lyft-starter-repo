import unittest
from datetime import datetime

from engines.capulet import Capulet
from engines.sternman import Sternman
from engines.willoughby import Willoughby

from batteries.nubbin import Nubbin
from batteries.spindler import Splinder

from tires.carrigan import Carrigan
from tires.octoprime import Octoprime


class TestCapulet(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0

        engine = Capulet(last_service_mileage, current_mileage)
        self.assertTrue(engine.engine_should_be_serviced())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0

        engine = Capulet(last_service_mileage, current_mileage)
        self.assertFalse(engine.engine_should_be_serviced())

class TestWilloughby(unittest.TestCase):

    def test_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0

        engine = Willoughby(last_service_mileage, current_mileage)
        self.assertTrue(engine.engine_should_be_serviced())

    def test_engine_should_be_serviced(self):
        current_mileage = 60000
        last_service_mileage = 0

        engine = Willoughby(last_service_mileage, current_mileage)
        self.assertFalse(engine.engine_should_be_serviced())
class TestSterman(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        warning_light_is_on = True
        engine = Sternman(warning_light_is_on)
        self.assertTrue(engine.engine_should_be_serviced())

    def test_engine_should_not_be_serviced(self):
        warning_light_is_on = False
        engine = Sternman(warning_light_is_on)
        self.assertFalse(engine.engine_should_be_serviced())

class TestSplinder(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)

        battery = Splinder(last_service_date)
        self.assertTrue(battery.battery_should_be_serviced())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        battery = Splinder(last_service_date)
        self.assertFalse(battery.battery_should_be_serviced())

class TestNubbin(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        battery=Nubbin(last_service_date)
        self.assertTrue(battery.battery_should_be_serviced())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        battery = Nubbin(last_service_date)
        self.assertFalse(battery.battery_should_be_serviced())

class TestCarrigan(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        wear_array = [0.5, 1, 0.8, 0.9]

        tire = Carrigan(wear_array)
        self.assertTrue(tire.tire_should_be_serviced())

    def test_tire_should_not_be_serviced(self):
        wear_array = [0.5, 0.8, 0.2, 0.4]

        tire = Carrigan(wear_array)
        self.assertFalse(tire.tire_should_be_serviced())

class TestOctoprime(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        wear_array = [0.5, 1, 0.8, 0.9]

        tire = Octoprime(wear_array)
        self.assertTrue(tire.tire_should_be_serviced())

    def test_tire_should_not_be_serviced(self):
        wear_array = [0.5, 1, 0.2, 0.4]

        tire = Octoprime(wear_array)
        self.assertFalse(tire.tire_should_be_serviced())

if __name__ == '__main__':
    unittest.main(verbosity=2)

# TestCapulet.run()
