# try/except ex1
def exp():

  num = input("Enter base: ")
  exponent = input("Enter exponent: ")

  try: 
    num = int(num)
    exponent = int(exponent)
  except:
    print("Not a valid number!")
    return exp()

  return num ** exponent

print(exp())

# FizzBuzz
for i in range (101):
  ans = ""
  if i % 3 == 0: ans += "Fizz"
  if i % 5 == 0: ans += "Buzz"

  print(ans or i)

# ex 2
def pay():
  hours = input("Enter hours: ")
  rate = input("Enter rate: ")
  try:
    hours = int(hours)
    rate = int(rate)
  except:
    print("Not a valid number!")
    return pay()

  if hours > 40: rate *= 1.5
  return "Pay: $" + str(hours * rate)

print(pay())

# ex 3
def grade():
  score = input("Enter score between 0 and 1: ")

  try:
    score = float(score)
  except:
    print("Enter valid score! <3")
    return grade()
  
  if score > 1 or score < 0:
    print("Out of range! Baka!")
    return grade()

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


print(grade())