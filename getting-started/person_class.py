class Person:
  '''
  This is a demo of docstrings, which will get printed out, when you call the __doc__ method on the class
  For more information on creating documentation with python, see: https://peps.python.org/pep-0257/
  '''
  def __init__(self, name: str, age: int):
    '''
    I'M A CONSTRUCTOR!!!
    '''
    self.name = name
    self.age = age
    
  def birthday(self):
    '''
    takes 0 arguments and increments the age of the person by 1.
    '''
    self.age += 1
    
  def __str__(self) -> str:
    return f"{self.name} is {self.age} years old."
  
  # def __repr__(self) -> str:
  #   pass


def main():
  person1 = Person("John", 42)
  print(person1)
  person1.birthday()
  print(person1)
  print(person1.__str__())
  print(person1.__repr__())
  print(person1.__doc__)
  print(Person.__init__.__doc__)
  print(person1.birthday.__doc__)


if __name__ == '__main__':
  main()