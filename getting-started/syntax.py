def sneaking_snake_case():
  # pass => placeholder / Platzhalter
  pass

# This is a single-line comment //"Comment" in C#


'''
This is a
multiline
comment
in C# /* "Comment" */
'''


def indent_example():
  user_input = input("Bitte geben Sie ein Zahl ein: ")
  if not user_input.isdigit():
    try:
      print(user_input + " ist keine Zahl!")
    except Exception as err:
      print(err)
    finally:
      print("Dieser Text wird auf jeden Fall immer ausgegeben (außer er selbst wirft eine Exception)")
    print()
  else:
    print("Das ist eine Zahl!")

# {
# "name": "Alfons",
# "surname": "Mueller"
# }


# Variables
'''
Python ist im Gegensatz zu C# eine dynamisch-typisierte Sprache.
In Python muss eine Variable nicht mit einem "Keyword" erst deklariert werden!
Die Deklaration wird automatisch ausgeführt, wenn einer neuen Variablen ein Wert zugewiesen wird...
'''


def variables(n=42):
  i = "This is a string!"
  c = 3.14159
  e = 5 > 10 | True
  print([n, i, c, e])
  return [n, i, c, e]


### Type-Hinting
'''
Seit Python 3.5 können Sie ihren Variablen "Hinweise" zur typisierung geben.
Diese sorgen allerdings nicht für Typen-Sicherheit, sondern sind eher als hilfe
für andere Entwickler gedacht, die Ihren Code später weiter verwenden.
'''


def type_hinting(n: int = 42):
  i: str = "This is a string!"
  c: float = 3.14159
  e: bool = 5 > 10 | True
  print([n, i, c, e])
  return [n, i, c, e]

### Casting und Type-Functions
def casting(f = 42):
  u = int(f)
  n = float(f)
  return [f, u, n]


'''
!!! IMPORTANT !!!
Filenames in Python sollten NIE mit einer Zahl/Sonderzeichen anfangen.
===> this will create silly error messages when working with modules (imports)

## Naming Conventions

* Variables = snake_case
* Functions = snake_case
* Methods = snake_case
* Modules = snake_case
* Classes = PascalCase
* Constants = SCREAMING_SNAKE_CASE
'''
def naming():
  from hello import HelloWorld
  class MyCoolClass:
    this_is_a_static_variable = "This is a static-variable"

    def __init__(self):
      THIS_IS_A_CONSTANT = 42
      self.this_is_a_instance_variable = "this is a instance-variable"

naming()
print(__name__)