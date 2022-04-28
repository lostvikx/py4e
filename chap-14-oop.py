import math

# Parent class
class Dog:
  name = ""
  color = ""

  def __init__(self, name, color):
    self.name = name
    self.color = color

  def describe(self):
    print(f"I am a {self.color} dogo!")

  def hello(self):
    print(f"{self.name} says woof!")


# Child class
class Wolf(Dog):
  num_wolf = 1

  def pack(self):
    self.num_wolf += 1
    print(f"The {self.num_wolf} of us rule this area.")


jacky = Dog("Jacky", "white")

jacky.hello()
jacky.describe()

woo = Wolf("Valery", "white")

woo.hello()
woo.describe()
woo.pack()
# print(dir(woo))

# This looks good!
class Circle:
  radius = 0

  def __init__(self, c_len, type_length = "r"):
    if type_length == "r": 
      try:
        c_len = float(c_len)
      except:
        print("Error in converting number to float")
        quit()
      self.radius = c_len
    elif type_length == "d": self.radius = c_len / 2

  def circumference(self):
    return round(2 * math.pi * self.radius, 2)

  def area(self):
    return round(math.pi * self.radius ** 2, 2)

# Radius in cm by default
newCir = Circle(10)

def cirInit(instance):
  rad = instance.radius
  circum = instance.circumference()
  area = instance.area()

  print(f"radius: {rad}cm\ncircumference: {circum}cm\narea: {area}cm^2")

cirInit(newCir)
