# Frage 1
def addition(zahl1, zahl2):
  return zahl1 + zahl2
  
# Frage 2
import math
print(f"Der Wer von Pi ist: {math.pi}")

# Frage 3
zahl = 5.5555
print(f"{zahl:.3f}") # Ausgabe: 5.556
print(f"{zahl:.0%}") # Ausgabe: 556%
# voting_result = 22.47852
# print('test {:2.2%}'.format(voting_result))
# https://docs.python.org/3/tutorial/inputoutput.html

# Frage 4
'''
- if Anweisungen können mit und ohne runde Klammern geschrieben werden.
- In Python ist das Keyword für die alternative zum If 'elif' und NICHT 'else if' wie in C#
'''

# Frage 5
for i in range(100):
  pass
sammlung = 1,2,3,4,5
for i in sammlung:
  pass
  

# Frage 6
'''
Die richtigen Antworten sind:
- "w" wird zum Beschreiben einer Datei benutzt. Ein bereits existierender Inhalt wird überschrieben.
- "x" wird zum erstellen einer Datei benutzt. Existiert die Datei bereits, wird eine Fehlermeldung ausgegeben.
'''

# Frage 7
'''
dictionaries sind:
- mutable
- ordered
- unordered
'''

# Frage 8
def funktion02(a, b) -> int:
  c = a + b
  print(c)
  return c
'''
Antwort:
- Es handelt sich um Funktion
- "a" und "b" sind parameter und MÜSSEN übergeben werden
'''

# Frage 9
'''
a. Mit der Import-Funktion kann der Inhalt eines anderen Python-Moduls für das aktuelle Modul bereit gestellt
werden.
b. Mit der Import-Funktion können Bibliotheken eingebunden werden.
c. Mit der Import-Funktion kann auch nur eine Funktion eines anderen Python-Moduls bereitgestellt werden.
'''

# Frage 10
'''
- Lists sind ordered
- Lists erlauben duplikate
- Lists sind indiziert
'''

# Frage 11
'''
Text lesen und überschreiben = r+
'''

# Frage 12
'''
- Sets sind immutable - Wahrscheinlich nicht richtig
- Sets erlauben keine duplikate
- Sets sind nicht geordnet
'''

# Frage 13
'''
s. getting-started/types
'''

# Frage 14
'''
str to float = float("4.235")
'''

# Frage 15
zahl1 = 15
zahl2 = 0
try:
  erg = zahl1 / zahl2
  print(erg)
except ZeroDivisionError:
  print('Teilung durch 0 nicht möglich.')
except:
  print('Allgemeiner Fehler.')
else:
  print('Kein Fehler aufgetreten.')
finally:
  print('Berechnung abgeschlossen.')

'''
a. Mit Hilfe des "try" wird versucht, einen eventuellen Ausnahmefehler abzufangen.
b. Der Code-Block zu "else" wird nur ausgeführt, wenn kein Ausnahmefehler vorlag.
'''

# Frage 16
'''
tuple sind:
- indiziert
- unmutable
'''

# Frage 17
zahlen = [19, 20, 30, 40, 22]
summe = 0
for zahl in zahlen:
  summe += zahl
print(summe)
'''
increment operator:
  +=
'''

# Frage 18
'''
++ und -- nicht in python
'''

# Frage 19
'''
python ist case-sensitive
'''

# Frage 20
'''
Python ist KEINE compiler-sprache
'''

# Frage 21
'''
Funktionen müssen in der Funktionssignatur (Definition) keinen Rückgabewert enthalten.
'''

# Frage 22
'''
Der Name "Python" kommt aus Monty Python
'''

# Frage 23
'''
Pyton ermöglicht objektorientiertes Programmieren.
'''

# Frage 24
'''
Python ist weakly-Typed.
'''