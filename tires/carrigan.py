from tire import Tire

class Carrigan(Tire):
  def __init__(self, wear_array):
    super().__init__(wear_array)
    self.wear_array = wear_array

  def tire_should_be_serviced(self):
    for wear_value in self.wear_array:
      if wear_value >= 0.9:
        return True
    return False