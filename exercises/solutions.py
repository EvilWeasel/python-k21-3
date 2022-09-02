def generate_fibonacci_sequence(ammount: int = 10000):
  i = 1
  fib = []
  if ammount <= 0:
    return fib
  elif ammount == 1:
    fib = [1]
  elif ammount == 2:
    fib = [1,1]
  elif ammount > 2:
    fib = [1,1]
    while i < (ammount - 1):
      fib.append(fib[i] + fib[i-1])
      i += 1
  return fib


def main():
  pass
  # print(generate_fibonacci_sequence())

if __name__ == '__main__':
  main()