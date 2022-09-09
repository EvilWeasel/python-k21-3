class Car:
  def __init__(self, color, manufacturer, make):
    self.color = color
    self.manufacturer = manufacturer
    self.make = make
    
  def __str__(self) -> str:
    return f"{self.color}, {self.manufacturer}, {self.make}"
