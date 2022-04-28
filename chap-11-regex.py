import re

# Two important methods
re.search("exp", str)  # Returns a boolean 
re.findall("exp", str)  # Returns a list of matches

from_str = "From viknegi0@gmail.com Sun Sep 5"
domain = re.findall("^From .*@(\S+)", from_str)
print(domain)

# \S == [^ ]

# Find max confidence number
try:
  hand = open("./src/mbox-short.txt", "r")
except:
  print("err opening file")
  quit()

num_list = list()

for line in hand:
  line = line.strip()
  conf_num = re.findall("^X-DSPAM-Confidence: ([0-9\.]+)", line)

  if len(conf_num) <= 0: continue

  try:
    float_num = float(conf_num[0])
  except:
    print("convert to float err")
    quit()
  
  num_list.append(float_num)

print(f"{max(num_list)} is the max conf-num")

x = "We just received $10.50 for a packet of cookies"
y = re.findall("\$[0-9.]+", x)
print(y[0])

# Search for lines that start with 'Details: rev='
# followed by numbers
# Then print the number if one is found

f_hand = open("./src/mbox-short.txt", "r")

for line in f_hand:
  line = line.strip()
  reg_details = re.findall("^Details: .+rev=(\d+)", line)
  reg_hours = re.findall("^From .* (\d{2}):", line)

  if len(reg_details) > 0: print(reg_details)

  if len(reg_hours) > 0: print(reg_hours)

reg = input("Enter a regex: ")

try:
  mbox_file = open("./src/mbox.txt", "r")
except:
  print("file open err")
  exit()

count = 0

for line in mbox_file:
  line = line.strip()
  reg_match = re.search(reg, line)

  if reg_match: count += 1

print(f"mbox.txt had {count} lines that matched {reg}")

# find avg new revision in mbox
fname = input("Enter file name: ")

try:
  fhandle = open(f"./src/{fname}", "r")
except:
  print("open file err")
  quit()

nums = list()

for line in fhandle:
  line = line.strip()
  reg = re.findall("^New Revision: (\d+)", line)

  if len(reg) > 0:
    reg = int(reg[0])
    nums.append(reg)

avg = sum(nums) // len(nums)

print(f"avg new revision: {avg}")