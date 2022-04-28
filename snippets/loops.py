# Loop control - break
while (True):
  line = input("> ")
  if (line == "done"): break

print("end!")

# Loop control - continue
# Continue ends the current iteration and jumps to the top of the loop, starting the next iteration

i = 5
while i > 0:
  if (i == 3):
    print("mid")
    i -= 1  # This is imp, else infinite loop
    continue
  print(i)
  i -= 1

# The "is" operator is like ===, checks value and type
# Only use "is" on Booleans or None types
smallest = None
for num in [12, 43, 22, 51, 22, 49]:
  if (smallest is None or num < smallest):
    smallest = num

print(smallest)