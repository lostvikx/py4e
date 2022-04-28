def power(a, b):
  return a ** b

print(power(5, 2))

n = 5 / 2
print(type(n)) # float

# input
name = input("Enter name: ")

print("Hey", name.capitalize())

# elevator converter program
inp_floor = input("Which floor? ")
# input gets us a string
usf = int(inp_floor) + 1
print("Floor in US:", usf)

def cel_to_far():
  cel = input("Enter temperature in celcius: ")
  fah = (int(cel) * 9 / 2) + 32
  print(fah)

cel_to_far()

width = 17
height = 12.0
print(width//2) # Math.floor(width/2)
print(width/2.0)  # 8.5
print(height/3)  # 4.0
print(1 + 2 * 5)  # 11

# input type outputs str, division type outputs float
num_inp = input("give a number\n")
ans = int(num_inp) / 1
print(type(num_inp), ans, type(ans))