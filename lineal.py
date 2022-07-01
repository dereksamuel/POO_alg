from random import random


import random


def lineal_search(list, final_point):
  match = False # 1

  for item in list: # list O(n)
    if (item == final_point):
      match = True
      break

  return match


if __name__ == "__main__":
  list_size = int(input("What is the size list?"))
  final_point = int(input("What is the final point of your list?"))

  array = [random.randint(0, 100) for item in range(list_size)]
  found = lineal_search(array, final_point)

  print(array)
  print(f"The element {final_point} {'is' if found else 'is not here'}")

