# Python Modules #
import re
from webbrowser import open
#from datetime import *
from datetime import datetime
from platform import system as plt

## Built-In Module ##
"""
Python liefert bereits einige Module mit, die vor Verwendung gesondert importiert werden
müssen. Der Grund hierfür ist einen Funktionsüberfluss und entsprechende 
Performanceeinschränkungen zu verhindern. Eine Liste aller dieser Module findet sich hier:           
  https://docs.python.org/3/py-modindex.html
"""
def builtin_modules():
  if plt() == 'Linux':
    open('https://docs.python.org/3/py-modindex.html')
    print(datetime.now() \
      .strftime("Today is %A, %d. of %B, %Y.\nYour local time is %H:%M"))
    
## Eigene Module ##
"""
Module sind nichts weiter als Python Skripte. Das bedeutet also um eigene Python Skripte
als Module zu laden ist es ausreichend, wenn das gewünschte Modul im selben Ordner
vorliegt. So kann das Skript dann wie ein Modul importiert werden.
"""
def own_modules():
  from my_complex import MyComplex
  # from ..my_first_consoleapp.consoleapp import main
  c1 = MyComplex(42, 4)
  c2 = MyComplex(-9, 7)
  print(c1.add(c2))

### Python 2 Hackery for relative Paths ###
# import sys, os
# sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Common'))
# import Common


## Externe Module ##
"""
Externe Module sollten über den "pip" Python Packet Manager heruntergeladen werden.
Dies geschieht über die Shell/ Bash über den Befehl:
                pip install <paketname>                 aktuelle Version des Moduls
                    Bsp: pip install numpy
Das Paket wird (wenn nicht virtuelle Umgebungen verwendet werden) im Directory 
"/lib/site-packages" des Python Ordners gespeichert.              
#py -m pip install -> workaround
"""
def external_modules():
  import numpy as np
  arr = np.array([[0,1,0,0], [0,0,1,0]])
  print(arr)

    
def main():
  # builtin_modules()
  builtin_modules()

if __name__ == '__main__':
  main()