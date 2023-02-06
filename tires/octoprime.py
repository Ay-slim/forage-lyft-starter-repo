from tire import Tire

class Octoprime(Tire):
  def __init__(self, wear_array):
    super().__init__(wear_array)
    self.wear_array = wear_array

  def tire_should_be_serviced(self):
    if sum(self.wear_array) >= 3:
      return True
    return False