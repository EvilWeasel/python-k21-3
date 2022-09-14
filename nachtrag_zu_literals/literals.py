import gc
import sys

def main():
  var_mainobj = {"name": "foo", "lastname": "bar"}
  ### literals
  var_mainref = var_mainobj
  var_mainref2 = var_mainobj
  var_main1 = 32
  var_main2 = 32
  var_mainfloat = 5.45
  var_mainimag = 5j
  var_mainstr = "hello"
  var_mainstrref = var_mainstr
  var_mainstrref1 = var_mainstr
  var_mainunicode = u"hello"
  # var_mainnone = None

  ### literal-like expressions
  var_main3 = -8
  var_maincomplex = 10+7j

  ### displays
  my_list = []
  my_list1 = [1,2]
  my_list2 = [x for x in var_mainobj]
  
  my_tuple = ()
  my_tuple1 = (1,2)
  my_tuple1 = 1,2,3,4,5,6,7,8
  
  my_dict = {}
  my_dict1 = {"foo": "bar"}
  
  my_set = {"foo", "bar"}

  print("Refcount for object is:")
  print(sys.getrefcount(var_mainstr)-1)
  
# varx = var_mainobj
# var1 = 10

def circular_referencing():
  class A:
    def display(self):
      print(f"A: self: {hex(id(self))}, b: {hex(id(self.b))}")
    def __del__(self):
      print("ObjA deleted")
  class B:
    def display(self):
      print(f"B: self: {hex(id(self))}, a: {hex(id(self.a))}")
    def __del__(self):
      print("ObjB deleted")

  # 2 obj, diffrent classes
  a = A()
  b = B()
  
  # references to each other
  a.b = b
  b.a = a
  
  # show heap memory address
  a.display()
  b.display()
  
  # delete objs
  del a
  del b

  print("hello")
  print("hello")
  print("hello")
  print("hello")
  print("hello")

if __name__ == '__main__':
  # main()
  circular_referencing()