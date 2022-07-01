class Person:
  def __init__(self, name, age, height, sex, superpower):
    self.name = name
    self.age = age
    self.height = height
    self.sex = sex
    self.superpower = superpower

  def go(self):
    print("I am walking")


class Cyclist(Person):
  def __init__(self, name, age, height, sex, superpower):
    super().__init__(name, age, height, sex, superpower)

  def go(self):
    print("I am going in my cycle 🚲")


def main():
  person = Person("Iris Glue", 18, 130.0, "Male", "Strenght")
  person.go()

  cyclist = Cyclist("Jean Glue", 8, 150.5, "Male", "Fly")
  cyclist.go()


if __name__ == "__main__":
  main()

