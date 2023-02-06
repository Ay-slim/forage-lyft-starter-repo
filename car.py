from engine import Engine
from battery import Battery
from tire import Tire

class Car(Engine, Battery, Tire):
    def __init__(self, engine, battery, tire):
        self.engine = engine
        self.battery = battery
        self.tire = tire
    
    def needs_servicing(self):
        return self.engine.engine_should_be_serviced() or self.battery.battery_should_be_serviced() or self.tire.tire_should_be_serviced()
