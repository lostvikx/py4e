nums = [11, 27, 39, [2, 4], 50]

# isinstance() is important
for i in range(len(nums)):
  if isinstance(nums[i], list):
    print("found a nested list", nums[i])
    continue

  nums[i] *= 2

print(nums)

# exercise
# chop
test_arr = [2, 5, 6, 8]
def chop(arr):
  del arr[0]
  del arr[len(arr) - 1]

# chop(test_arr)
print(test_arr)

# middle
def middle(arr):
  new_arr = arr[1:]
  return new_arr[:len(new_arr) - 1]

print(middle(test_arr))

fname = input("Enter a file name: ")

try:
  file_handle = open(f"./src/{fname}")
except:
  print("error reading the file")
  quit()

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

for line in file_handle:
  line = line.strip()
  words = line.split()

  if len(words) == 0 or words[0] != "From" or len(words) < 3 or words[2] not in days: continue

  print(words[2])

# romeo.txt
try:
  file_handle = open("./src/romeo.txt", "r")
except:
  print("cannot open romeo.txt}")
  quit()

unique_words = []

for line in file_handle:
  line = line.strip().split()
  # print(line)
  for w in line:
    if w not in unique_words: unique_words.append(w)

unique_words.sort()
print(unique_words)

# From email counter
file_name = input("Enter file name: ")

try:
  fhandle = open(f"./src/{file_name}", "r")
except:
  print("file not found")
  quit()

count = 0

for line in fhandle:
  line = line.strip()
  if line.startswith("From") and not line.startswith("From:"):
    words = line.split()
    count += 1
    print(words[1])

print(f"There were {count} lines with From as the first word")

# rewrite
nums = []

while True:
  num_input = input("Enter a number: ")
  try:
    num_input = float(num_input)
    nums.append(num_input)
  except:
    complete_message = ["done", "Done", "complete", "Complete", "ok", "OK", "Okay", "okay"]
    if num_input in complete_message: 
      print(f"Max: {max(nums)}")
      print(f"Min: {min(nums)}")
      break
    else:
      print("not a valid number")
      continue

print("list:", nums)