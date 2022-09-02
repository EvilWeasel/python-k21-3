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
    








def main():
  # x = input("Enter the first number.")
  # y = input("Enter the second number.")
  # operator = input("Enter the operator (+ - * / % ** //) to select the operation.")
  # print(calculate(x, y, operator))
  pass

if __name__ == '__main__':
  main()