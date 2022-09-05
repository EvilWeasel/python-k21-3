# Inheritance
class Polygon:
  '''
  Ein Polygon (Vieleck) ist eine Fläche die durch eine endliche Anzahl an gerade Linien definiert ist.
  '''
  def __init__(self, sides: list[int]):
    self.sides = sides
  
  def display_info(self):
    print("A polygon is a two-dimensional shape with straight lines.")
    
  def get_perimeter(self):
    return sum(self.sides)

class Triangle(Polygon):
  def __init__(self, sides: list[int], isRight: bool):
    super().__init__(sides)
    self.isRight = isRight
  
  def display_info(self):
    print("A triangle is a polygon with 3 sides and 3 vertices.")


class Quadrilateral(Polygon):
  def display_info(self):
    print("A quadrilateral is a polygon with 4 sides and 4 vertices.")


def main():
  pol1 = Polygon([4,5,4,5])
  pol1.display_info()
  print(pol1.get_perimeter())
  tri1 = Triangle([5,5,10], isRight=False)
  tri1.display_info()
  print(tri1.get_perimeter())
  qua1 = Quadrilateral([4,8,4,8])
  qua1_ref = qua1
  qua2 = Quadrilateral([2,4,2,4])
  qua1.display_info()
  print(qua1.get_perimeter())
  
  print("-----")
  print(dir(Quadrilateral))
  print(dir(qua1))
  
  print(f"id of qua1: {id(qua1)}\nid of qua2: {id(qua2)}\nid of qua1_ref: {id(qua1_ref)}")


if __name__ == '__main__':
  main()