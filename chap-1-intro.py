# assignment
x = 2
print(x)
x += 2
print(x)

# conditional
y = 5
if x >= 10:
  print("10 or more")
else:
  print("less than 10")

# while loop
z = 5
while z > 0:
  print(z)
  z -= 1
print("Blastoff!")

# euclid's algo to calc gcd or hcf
def hcf(a, b):
  if b == 0: 
    return a
  else: 
    return hcf(b, a % b)

print(hcf(25, 40))  # 5
