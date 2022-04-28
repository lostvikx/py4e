import math
from random import random, choice, randint

def deg_to_rad(deg):
  return deg * (2 * math.pi / 360)

radian = deg_to_rad(45)

radian = math.radians(45)

print(round(math.sin(radian), 2))

for i in range(5):
  num = random() * 10
  print(math.floor(num))

# select random element from arr
arr = [109, 260, 351, 258, 122, 512, 729]

select = choice(arr)
print(select)

# random in range inclusive
rand_int = randint(0, 10)
print(rand_int)

def repeat_lyrics():
  print_lyrics()
  print_lyrics()

def print_lyrics():
  print("I'm a lumberjack, and I'm okay.")
  print('I sleep all night and I work all day.')

repeat_lyrics()

# exercise
def computepay(hours, rate):
  extra_pay = 0
  extra_time_rate = rate * 1.5

  if (hours > 40):
    extra_time = hours - 40
    extra_pay = extra_time * extra_time_rate
    
  return "Pay: $" + str((rate * 40) + extra_pay)

# rate is $10 per hour
print(computepay(45, 10))


def computegrade(score):
  score = float(score)

  if score > 1 or score < 0:
    print("Out of range! Baka!")
    return computegrade(float(input("Enter within 0 to 1 range:\n")))

  if score >= 0.9:
    return "A = Absolute class"
  elif score >= 0.8:
    return "B = Bright future"
  elif score >= 0.7:
    return "C = Can do much better"
  elif score >= 0.6:
    return "D = Dumb fuck"
  else:
    return "F = Fuck you"

print(computegrade(0.7))