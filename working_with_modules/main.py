#import module1
#from module1 import Person, hello_print
# import models.person
# from models import person
# import models.old.old_person
# from models.old.old_person import Person
# import models.person
# from models import person
import models
from models import Car, Person
import package3

def main():
  print("Start")
  person1 = Person(42, "Harry", "Muster", 24, "harry-m@aol.de")
  print(person1)
  # hello_print()
  package3.test_function_package3()
  package3.test_function_package3_2()


if __name__ == '__main__':
  main()