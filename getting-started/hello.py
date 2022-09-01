# Console.WriteLine()
# print("Hello World!")

# class HelloWorld
# {
#   public int alter = 0;
# }

class HelloWorld:
  def greet(self):
    print("Hello World!")

def main():
  greeter = HelloWorld()
  greeter.greet()
  print(__name__)


if __name__ == '__main__':
  main()
