class Rectangle:
  def __init__(self, base, height):
    self.height = height
    self.base = base

  def area(self):
    return self.base * self.height

class Shape(Rectangle):
  def __init__(self, side):
    super().__init__(side, side)

    pass

if __name__ == "__main__":
  rectangle = Rectangle(8, 3)
  print(rectangle.area())

  shape = Shape(10)
  print(shape.area())

# Here my challenge:

class Animals:
  def __init__(self, name, cientific_name, age, is_cute, height, type, kind_of_food="Something"):
    self.name = name
    self.cientific_name = cientific_name
    self.age = age
    self.is_cute = is_cute
    self.height = height
    self.kind_of_food = kind_of_food
    self.type = type

  def eating(self):
    return f"I'm eating {self.kind_of_food}"

  def speaking(self):
    if self.type == "loro":
      return "I am speaking"
    else:
      return "I can't speak"


class Vegetarians(Animals):
  def __init__(self, name, cientific_name, age, is_cute, height, type):
    super().__init__(name, cientific_name, age, is_cute, height, type, "Vegetables")


class Carnivores(Animals):
  def __init__(self, name, cientific_name, age, is_cute, height, type):
    super().__init__(name, cientific_name, age, is_cute, height, type, "Meat")
    self.carnivore_type = None

  def get_food(self, type):
    if type == "HUNTING":
      self.carnivore_type = "Depredador"
    else:
      self.carnivore_type = "Carronero"

    return f"I am getting my sweet food {type}"

if __name__ == "__main__":
  loro = Vegetarians(
    name="PericoJeje",
    cientific_name="Psittacoidea",
    age=3,
    is_cute=True,
    height=15.26,
    type="loro"
  )
  print(loro.eating())
  print(loro.speaking())

  lion = Carnivores(
    name="King",
    cientific_name="Panthera leo",
    age=13,
    is_cute=True,
    height=250.9,
    type="lion"
  )
  print(lion.eating())
  print(lion.speaking())
  print(lion.get_food("HUNTING"))
