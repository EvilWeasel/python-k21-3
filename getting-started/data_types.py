# Data-Types: Overview
'''
In Python sind viele, der uns bereits bekannten Datentypen bereits implementiert.
Viele Datentypen, die wir aus C# kennen, werden wir hier allerdings "vermissen".

* Numbers
  - integer ==> int() = 42
  - float ==> float() = 42.420
  - complex numbers ==> complex() = 8j
* Text
  - string ==> str() = "hello" = 'hello' = 'a'
* Logical
  - boolean ==> bool = True | False
* Collections
  - List ==> list = [1, 2, 3, {"name": "Herbert"}, ["a", "b", "c"]]
  - Tuple ==> tuple = (1, 2, 3)
  - Set ==> set = {1,2,3,4,5,6}
* None

* Maybe you can find some more..
'''

# my_bytes = bytes("Python is the best Language ever!", 'utf-8')
# print(my_bytes)

### Numbers
'''
Um zwei Zahlen zu addieren, ist es in Python nicht zwangsläufig notwendig
die Variablen zu Casten. Python macht bei Mathematischen Operationen zwischen zwei
Zahlen eine Art "Type-Cohersion" wie JavaScript.
int -> float -> complex
'''
def casting_works():
  print(int(1.7), float(99), complex(42))

# def casting_fails():
#   print(int(4j+3), float(4j+3))


### Math-Module
'''
Das Math-Modul beinhaltet eine Sammlung an Hilfsfunktionen und Konstanten,
um Mathematische Operationen durchzuführen.

Constants:
* PI
* e
* infinity
* nan
* tau
* ...

Useful functions:
* ceil(x) => round up
* floor(x) => round down
* sqrt(x) => square root
* fsum(collection) => sums all elements
* gcd(x,y) => greatest common divisor
'''
def more_maths():
  import math

  PI = math.pi
  E = math.e

  print(f"{PI} hoch {E} = {PI**E}")
  print(f"Die Quadratzahl von {PI} ist {math.sqrt(PI)}")
  print(f"Der groesste gemeinsame Teiler von 9 und 180 ist {math.gcd(9,180)}")

# more_maths()

### Strings
'''
* use "" or '' - does not matter
* strings can be concatenated (Verkettet +)
* strings may be formatted with the format()-function or the f-string-literal => f"{variable_name}"
* strings are immutable => nicht veränderbar
* string can be indexed with eg. my_string[0]
* string surrounded by tripple-quotes are so called 'docstrings' (or multiline docstrings)

more at: https://docs.python.org/3/library/stdtypes.html#string-methods
'''
def strings_as_collections(my_string = "Hello World!"):
  '''
  takes a string as input and outputs all characters on individual lines
  '''
  for char in my_string:
    print(char)

def string_methods():
  og_string = "This Sentence is false, determined by me."
  print(og_string.upper())
  print(og_string.lower())
  print(og_string.replace('false','true'))
  split_string = og_string.split(',')
  for string in split_string:
    print(string.strip())
  for string in split_string:
    print(string.capitalize())


def check_bool():
  '''
  Wenn eine Variable einen (oder auch mehrere) Werte zugeordnet ist, dann wird daraus,
  wenn man diese in den Constructor von bool() gibt ein True.
  Generell kann man sagen, dass ein "leerer" Datentyp False returnt, wenn er zu bool konvertiert wird.
  '''
  arguments = [
    "True", #True
    "False", # True
    "", # False
    1, # True
    -5, # True
    0, # False
    (), # False
    (1,2,3), # True
    {}, # False
    {"name": "Herbert"}, # True
    [], # False
    None # False
  ]
  # arguments?.ForEach()
  # propertyChanged?.Invoke()
  if arguments:
    for a in arguments:
      print(f"{a} evaluates to {bool(a)}")

check_bool()