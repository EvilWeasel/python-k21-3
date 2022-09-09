def test_function():
  print("hi")
  
def test_name():
  print(f"Ich werde in {__name__} ausgeführt!")
  

a = 5

def main():
  test_function()
  test_function()
  test_function()
  test_name()

if __name__ == '__name__':
  main()