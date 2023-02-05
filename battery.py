from abc import ABC, abstractmethod

class Battery(ABC):
  def __init__(self, last_service_mileage, current_mileage, warning_light_on):
    self.last_service_mileage = last_service_mileage
    self.current_mileage = current_mileage
    self.warning_light_on = warning_light_on
  
  @abstractmethod
  def battery_needs_servicing(self):
    pass