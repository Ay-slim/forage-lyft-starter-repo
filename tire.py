from abc import ABC, abstractmethod

class Tire(ABC):
  def __init__(self, wear_array):
    self.wear_array = wear_array

  @abstractmethod
  def tire_should_be_serviced(self):
    pass