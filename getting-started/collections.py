even_numbers = [x for x in range(1, 101) if x % 2 == 0 and
                x > 10]

# print(even_numbers)

# Collections
'''
In aller Kürze:
Collection        Liste[]     Tupel()     Set{}       Dict{}      String
geordnet?         Ja          Ja          Nein        Ja          Ja
indiziert?        Ja          Ja          Nein        Schlüssel*  Ja
veränderbar?      Ja          Nein        Nein        Ja          NEIN!!!
doppelte werte?   Ja          Ja          Nein        Nein*       Ja
'''


def collections():
  tuple_example = (1, 2, 3, 4, 4, 4, 5, 6, 6, 7, 8)
  list_example = ["Josef", "K.", 46, False]
  set_example = {"Heinrich", "Faust", 420, None,
                 420, None, None, None, "Heinrich", "Faust"}
  dict_example = {"Vornamen": "Arthur",
                  "Nachnamen": "Dent", "Alter": 42, "Lebt": True}
  string_example = "safjlkdjllks"
  dict_example["Vornamen"] = "Albert"
  print(set_example)
  print(dict_example)
  print(tuple_example)


def character_sheet():
  all_names = {"Toaster", "Fantastico", "Mochok"}

  char_from_csv = "Mochog,42.2846,Warrior,Human,Lagrand,420.247,1377.573,"\
      "Lame Copper Sword,Invisible Helm of Brilliance,Cool Shirt,-,10,128,12"
  char = char_from_csv.split(",")

  char_position = (char[4], int(float(char[5])), int(float(char[6])))

  char_dict = {
      "info":
      {
          "name": char[0],
          "level": int(float(char[1])),
          "class": char[2],
          "race": char[3],
      },
      "location": char_position,
      "stats":
      {
          "equipment":
          {
              "weapon": char[7],
              "head": char[8],
              "chest": char[9],
              "pants": char[10]
          },
          "power":
          {
              "agility": int(char[11]),
              "intelligence": int(char[12]),
              "strength": int(char[13])
          }
      }
  }
  if char_dict["info"]["name"] not in all_names:
    for key in char_dict.keys():
      print("\n" + "* " * 3 + key.upper() + " *" * 3)
      if type(char_dict[key]) == dict:
        for subkey in char_dict[key].keys():
          if type(char_dict[key][subkey]) == dict:
            print("\n" + subkey.upper() + "\n")
            for item in char_dict[key][subkey].keys():
              print(f"{item.capitalize()}:\t{char_dict[key][subkey][item]}")
          else:
            print(f"{subkey.capitalize()}:\t\t{char_dict[key][subkey]}")
      else:
        print(
          f"Zone:\t\t{char_dict[key][0]}\nX-Position:\t{char_dict[key][1]}\nY-Position:\t{char_dict[key][2]}")

  else:
    print("Your name is occupied. Please select another name.")


def access_collections():
  tuple_example = ("Winston", "Smith", 52, True)
  list_example = ["Josef", "K.", 46, False]
  set_example = {"Heinrich", "Faust", 72, None}
  dict_example = {"Vorname": "Arthur",
                  "Nachname": "Dent", "Alter": 42, "Lebt": True}
  string_example = "ABCDEFGHIJKLMNOPQURSTUVWXYZ0123456789"

  # Tuple
  print(tuple_example)
  # tuple_example[1] = "Lauch"
  workaround_list = list(tuple_example)
  workaround_list[1] = "Lauch"
  tuple_example = tuple(workaround_list)
  print(tuple_example)

  # Listen
  print(list_example)
  list_example[1] = "Lauch"
  print(list_example)

  # Sets
  print(set_example)
  # set_example[1] = "Lauch"
  set_example.remove("Faust")
  set_example.add("Lauch")
  print(set_example)

  # Dict
  print(dict_example)
  dict_example["Nachname"] = "Lauch"
  print(dict_example)

  # Strings
  # string_example[1] = "L"
  print(string_example)
  workaround_string = string_example[0]
  workaround_string += "L"
  for i in range(2, len(string_example)):
    workaround_string += string_example[i]
  string_example = workaround_string
  print(string_example)


'''
Redundanztoleranz:
Doppelte Werte werden in allen Aufzählungen erlaubt, 
jedoch ignorieren Sets doppelte Werte, Wörterbücher
ignorieren doppelte Schlüssel.
'''


def duplicates_in_collections():
    # TUPLE
  tuple_example = ("A", "N", "A", "N", "A", "S")
  print(tuple_example)

  # LIST
  list_example = ["A", "N", "A", "N", "A", "S"]
  print(list_example)

  # SET
  set_example = {"A", "N", "A", "N", "A", "S"}
  print(set_example)

  # DICT
  dict_example = {"A": 0,
                  "N": 1,
                  "A": 2,
                  "N": 3,
                  "A": 4,
                  "S": 5}
  print(dict_example)

  # STRING
  string_example = "ananas"
  print(string_example)


# Listen
'''
Zu Queues: https://docs.python.org/3/library/queue.html

List-Functions
list[i] = new_value
list.insert(index, new_value) => fügt den Wert an dem gewünschten Index hinzu
list.append(new_value) => Fügt den Wert am Ende der Liste hinzu
list.remove(value) => Entfernt das Element mit dem Wert
list.pop() => Entfernt das Element am Index (Default = Last)
my_list = list_a + list_b => Kombinieren von mehreren Listen
list.extend(another_collection) => fügt die Elemente der anderen Liste, der anfänglichen Liste am Ende hinzu
list.count(10) => gibt die Anzahl von Elementen mit dem angegebenen Wert, innerhalb der Liste an.
'''


def list_functions(list_length: int):
  list_a = []
  for i in range(list_length):
    list_a.append(i)
    if i % 2 == 0:
      list_a.remove(i)
  for i in range(list_length):
    if i % 2 != 0:
      list_a.insert(i - 1, i - 1)

  # Reihenfolge - immer wichtig!
  list_a.pop(int(list_length / 2))
  list_a.pop(0)
  list_a.pop()

  print(list_a)

# Tuple
'''
tuple.append(item)
tuple.count(item)
a, b, c = tuple
'''
def tuple_functions():
  my_tuple = ("Alfons", 420, None)
  a,b,c = my_tuple
  print(a)


def main():
  tuple_functions()


if __name__ == '__main__':
  main()
