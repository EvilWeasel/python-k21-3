class MyComplex:
  '''
  A complex number has two parts:
    - a real part => 42
    - an imaginary part => 8i
  '''
  def __init__(self, real: int, imag: int):
    self.real = real
    self.imag = imag
    

  def add(self, number: 'MyComplex') -> 'MyComplex':
    real = self.real + number.real
    imag = self.imag + number.imag
    result = MyComplex(real, imag)
    return result

  def __str__(self) -> str:
    return f"{self.real} + {self.imag}i"
    

  
def main():
  n1 = MyComplex(5, 6)
  n2 = MyComplex(-4, 2)
  result = n1.add(n2)
  print(result)

if __name__ == '__main__':
  main()