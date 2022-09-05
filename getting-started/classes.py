# Classes


class Cat:
  pass


class Dog:
  def __init__(self, name: str):
    '''
    Diese Methode ist ein Konstruktor, wie man ihn auch aus anderen Programmiersprachen kennt. Dabei ist der "self"-Parameter eine Referenz auf die Instanz des Objekts.
    Somit können wir den Instanzen der Klasse Variablen hinzufügen, die im Konstruktoraufruf entgegengenommen werden.
    '''
    self.name = name

  def bark():
    '''
    Das ist eine statische Klassenmethode, die keine Referenz auf die Instanz hat.
    Sie muss über die Klasse (Dog.bark()) aufgerufen werden.
    '''
    print("Woof!")
  
  def eat(self, food: str):
    print(f"{self.name} is eating {food}")
    
  # def race():
  #   return "Schäferhund"


def main():
  # In Python können Sie zur Laufzeit einem Objekt nach der Instanzierung weiter Attribute zuweisen, ähnlich wie in JS
  #cat1 = Cat()
  # cat1.name = "Mr. Whiskers"
  #cat2 = Cat()
  # cat2.name = "Mrs. Whiskers"
  dog1 = Dog("Fido")
  print(dog1.name)
  # dog1.bark() wirft einen Fehler, da es eine statische Methode ist und nicht der Instanz zugewiesen ist
  Dog.bark()
  dog1.eat("Italiener (voll special :D)")
  # print(Dog.race())

if __name__ == '__main__':
  main()