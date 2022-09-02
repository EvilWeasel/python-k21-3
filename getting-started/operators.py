# Arithmethic Operators
'''
+ Addition
- Subtraction
* Multiplication
/ Division
** Exponent
% Modulo
// Floor-Division

Additional Hackery eg.
<value> **(1/<nth-root>) = nth-root of <value>
'''
# print(18**(1/4))

def calculate(x: int, y: int, operator: str) -> float:
  '''
  This function takes in 2 integers and an operator-string as parameters and
  calculates the result based on the corresponding operator.
  Throws ValueError if x or y can't be converted to integers.
  '''
  try:
    x = int(x)
    y = int(y)
  except ValueError as ve:
    print("ERR: ", ve)
    return 0
  match operator:
    case '+':
      return x + y
    case '-':
      return x - y
    case '*':
      return x * y
    case '/':
      return x / y
    case '%':
      return x % y
    case '**':
      return x ** y
    case '//':
      return x // y
    case _:
      Exception("EXCEPTION!: No Operator given. ERROR-LEVEL: 8")
      return 0


# Assignment Operators
'''
  ## x = 4+2j
  ## x = "hello world"
  ## z = "abc"
    'AS - Operator'

  ## print(f"Typ von x:{type(x)}\nTyp von z:{type(z)}")
x = 4
x += 1
x -= 1
x *= 1
x /= 1
x //= 1
x %= 1
x **= 1
'''
def assignment_operators():
  for i in range(0,10000):
    if i < 10000:
      i += 1
    print(i)
  for j in range(9999,0,-1):
    if j > 0:
      j -= 1
    print(j)


# Logical Operators
'''
AND ==> True AND False => False
OR ==> True OR False => True
NOT ==> NOT True => False
'''
def collision_detection(entity_position = {"x": 0, "y": 10},\
  obstacle_position = {"x": 0, "y": 10}):
  # multiline-statements in python are possible with a backslash
  if entity_position["x"] == obstacle_position["x"] \
    and entity_position["y"] == obstacle_position["y"]:
    return True
  else:
    return False

# Identity Operator
'''
# In JS:
a{"name": "Herbert"} == b{"name": "Herbert"} TRUE
a{"name": "Herbert"} === b{"name": "Herbert"} False

# In Python:
is ==> true if both operands are the same object
is not ==> true if both operands are NOT the same object
https://docs.python.org/3/library/copy.html
'''
def identity_operators():
  a = [1,2,3]
  b = [1,2,3]

  c = a
  
  print(a is b) # False
  print(a is c) # True
  

# Membership Operators
'''
in => True if the value is in the sequence
not in => False if the value is in the sequence
'''
def membership_operator():
  a = ["Alfons", "Betty", "Charly"]
  print("Betty" in a)
  print("Darius" not in a)

# Bitwise Operators
'''
& ==> AND
| ==> OR
^ ==> XOR
~ ==> NOT
<< ==> bitwise left shift
>> ==> bitwise right shift
'''
def bitwise_operators():
  a = 60 # 60 => 0011 1100
  b = 13 # 13 => 0000 1101

  # bitwise AND
  c = a & b # 0000 1100 ==> 12
  print(c)
  # bitwise OR
  c = a | b # 0011 1101 => 61
  print(c)
  # bitwise XOR
  c = a ^ b # 0011 0001 => 49
  print(c)
  # bitwise NOT
  c = ~a # 1100 0011 => 195 ODER -61
  print(c)
  # bitwise left shift
  c = a << 2 # 1111 0000 => 240
  print(c)
  # bitwise right shift
  c = b >> 1 # 0000 0110 => 6
  print(c)





def main():
  # x = input("Enter the first number.")
  # y = input("Enter the second number.")
  # operator = input("Enter the operator (+ - * / % ** //) to select the operation.")
  # print(calculate(x, y, operator))
  # assignment_operators()
  bitwise_operators()

if __name__ == '__main__':
  main()