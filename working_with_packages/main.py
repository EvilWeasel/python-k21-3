import module1
from module2 import test_function as test_function2
from package1.module1_1 import test_function as test_function3

from package2.module2_1 import *

import package3

def test_name():
  print(f"Ich werde in {__name__} ausgeführt!")
# module1.test_function()
test_function2()
test_function_package2()
package3.test_function_package3()
package3.test_function_package3_2()

# print(module1.a)
# module1.test_name()
test_name()

