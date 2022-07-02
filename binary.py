import random


def binary_search(list, start, end, objective_id, counter1):
  print(f"searching {objective_id} between {list[start]} and {list[end - 1]}")
  print("counter1", counter1)
  if start > end:
    return None

  midle = (start + end) // 2 # cociente es entero
  id = list[midle]["id"]

  if id == objective_id:
    return list[midle]
  elif id < objective_id:
    return binary_search(list, midle + 1, end, objective_id, counter1 + 1)
  else:
    return binary_search(list, start, midle - 1, objective_id, counter1 + 1)


def sortById(item):
  return item["id"]


if __name__ == "__main__":
  list = [
    { "id": 154, "name": "David" },
    { "id": 3547454574558, "name": "Samuel" },
    { "id": 45454121, "name": "Catty" },
    { "id": 5456778787, "name": "Little" },
    { "id": 8945423278788, "name": "Asturat" }
  ]
  objective_id = int(input("What is the objective_id of your list?"))

  list.sort(key=sortById)
  found = binary_search(list, 0, len(list), objective_id, counter1=1)
  print(list)

  print(f"The element {f'with id {objective_id} is {found}' if found else 'is not here'}")

