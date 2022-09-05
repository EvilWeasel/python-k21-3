# Python Exercises

## Level 1

### Fibonacci-Numbers

Write a program that generates as much Fibonacci-Numbers as the user wants.

**Hint**: Fibonacci-Numbers are sequences of numbers, where the next number is the sum of the previous two numbers.

Example: [1,1,2,3,5,8,13,...]

Bonus: Write your Program in a way, so it can be used as a module as well as standalone.

## Level 2

### Collection: Map

(~15 Minuten)

Sie bekommen eine 5x5 große Karte in Form eines Tuples als Parameter.
Sie sollen diese Karte nun in der Konsole ausgeben. Dabei sollen alle Felder, die nicht
frei sind, mit einem "X" gefüllt werden, alle freien Felder erhalten ein " " (Leerzeichen).
Die eigene Position (des Spielers) wird durch ein "O" dargestellt.

Example:
  x xxx
  xo  x
  xxx x
      x
  xxxxx

```python
def aufgabe_4_3(own_position: tuple = (1,1), \
  free_spaces: tuple = ((0,1),(1,1),(1,2),(1,3),(2,3),(3,3),(3,2),(3,1),(3,0))):
  map = {}
  display = ""
  # Code goes here:

  print(display)
```

### Collections: Aufgabe 2

