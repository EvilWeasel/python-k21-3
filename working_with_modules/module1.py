class Person:
  def __init__(self, id: int, name: str, lastname: str, age: int, email: str):
    self.id = id
    self.name = name
    self.lastname = lastname
    self.age = age
    self.email = email
    
  def __str__(self) -> str:
    return f"{self.name} {self.lastname} ist {self.age} Jahre alt."

def hello_print():
  print("Hello")
  
