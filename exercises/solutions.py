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
  

def collections_map(own_position: tuple = (1,1), \
  free_spaces: tuple = ((0,1),(1,1),(1,2),(1,3),(2,3),(3,3),(3,2),(3,1),(3,0))):
  map = {}
  display = ""
  # Code goes here:
  for i in range(5):
    map.update({f"row {i+1}": []})
    for j in range(5):
      map[f"row {i+1}"].append({f"col {j+1}" : {"pos": (i,j), "obs": None}, "player": None })
      if (i, j) in free_spaces:
        map[f"row {i+1}"][j][f"col {j+1}"]["obs"] = False
      else:
        map[f"row {i+1}"][j][f"col {j+1}"]["obs"] = True
  
  for row in map.keys():
    for i in range(len(row)):
      if map[row][i][f"col {i+1}"]["obs"]:
        display += "X"
      elif map[row][i][f"col {i+1}"]["pos"] == own_position:
        display += "O"
      else:
        display += " "
    display += "\n"

  print(display)


def main():
  collections_map()
  # print(generate_fibonacci_sequence())

if __name__ == '__main__':
  main()