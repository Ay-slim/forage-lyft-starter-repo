from engine import Engine
from battery import Battery

class Car(Engine, Battery):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery
    
    def needs_servicing(self):
        return self.engine.engine_should_be_serviced() or self.battery.battery_should_be_serviced()
