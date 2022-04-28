# loop control - break
while (True):
  line = input("> ")
  if (line == "done"): break

print("end!")

# loop control - continue
# continue ends the current iteration and jumps to the top of the loop, starting the next iteration

i = 5
while i > 0:
  if (i == 3):
    print("mid")
    i -= 1  # this is imp, else infinite loop
    continue
  print(i)
  i -= 1

for i in [1, 2, 3, "done!"]:
  print(i)

friends = ["adriana", "abella", "chanel"]

for friend in friends:
  print("Hey " + friend.capitalize() + "!")

largest = -1
for num in [12, 43, 22, 51, 22, 49]:
  if (largest < num): largest = num

print(largest)

# find the avg
def avg(arr):
  sum = 0 
  count = 0
  for num in arr:
    sum += num
    count += 1
  
  return round(sum / count, 2)

print(avg([12, 43, 22, 51, 22, 49]))

arr = [12, 43, 22, 51, 22, 49]
avg = round(sum(arr) / len(arr), 2)
print(avg)

arr = [12, 43, 22, 51, 22, 49]
print("Min:", min(arr))
print("Max:", max(arr))

# "is" is like ===, checks value and type
# only use "is" on booleans or none types
smallest = None
for num in [12, 43, 22, 51, 22, 49]:
  if (smallest is None or num < smallest):
    smallest = num

print(smallest)

# exercise
total = 0
count = 0
avg = None

while True:
  num = input("> ")
  try:
    num = int(num)
    total += num
    count += 1
  except:
    if (num == "done"):
      avg = round(total / count, 2)
      print("Total:", total)
      print("Count:", count)
      print("Average:", avg)
      break
    else:
      print("invalid input")
      continue

num_list = []

while True:
  num = input("> ")
  try:
    num = int(num)
    num_list.append(num)
  except:
    if (num == "done"):
      print("Min:", min(num_list))
      print("Max:", max(num_list))
      break
    else:
      print("invalid input")
      continue

num_list = []
while True:
  num = input("> ")
  try:
    num = int(num)
    num_list.append(num)
  except:
    if num == "done":
      print("Total:", sum(num_list))
      print("Count:", len(num_list))
      print("Average", round(sum(num_list) / len(num_list), 2))
      print("Min:", min(num_list))
      print("Max:", max(num_list))
      break
    else:
      print("invalid input")
      continue

print("List:", num_list)
