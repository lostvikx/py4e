# this is a file handle, it lets us open, close, read, and write files from our python program
read_file = open("./src/test.txt", "r")

# we are only reading one line at a time
count = 0
for line in read_file:
  count += 1

print("Line Count: %d" % count)

# read whole file
text = read_file.read()
print(len(text))
read_file.close()

# searching through a file
# print comments from txt file
for line in read_file:
  line = line.strip()
  if line.startswith("#"): print(line)

# print if the line includes "love"
for line in read_file:
  line = line.strip()
  if "love" in line:
    print(line)

# does the same thing
for line in read_file:
  line = line.strip()
  if not "love" in line:
    continue
  print(line)

# the handle will work only if the file exists and you have to permission to read or write
fhand = open("./src/mbox.txt", "r")
# later we will use try and except to gracefully deal with situations where we attempt to open a file that does not exist.

count = 0
# the for loop reads the data not the fhand
# this can count the lines in any size file using little memory, since each line is read, counted, and then discarded
# for and while loops reads files in chuncks
for line in fhand:
  count += 1

print("Line count: %d" % count)

short_fhand = open("./src/mbox-short.txt", "r")

for line in short_fhand:
  line = line.strip()
  if line.startswith("From:"): print(line)

# startswith
for line in short_fhand:
  line = line.strip()
  # skip the "uninteresting" line
  if not line.startswith("From:"): continue
  # print our "interesting line"
  print(line)

# find
for line in short_fhand:
  line = line.strip()
  if line.find("@uct.ac.za") == -1: continue
  print(line)

fname = input("Enter a file name (without extension): ")

# using try and except to open a file is called the "Python way" of doing things
try:
  fhand = open("./src/%s.txt" % fname, "r")
except:
  print(f"The file {fname}.txt doesn't exist")
  quit()

# count subject lines
count = 0

for line in fhand:
  if line.startswith("Subject:"): count += 1

print(f"There are {count} subject lines in {fname}.txt")

fhand.close()

# write files
fout = open("./src/amanda.txt", "w")
fout.write("This is Amanda,\n")
fout.write("she is my neighbour, and I like her.\n")
fout.close()

# debugging tips
test_str = "1 2\t 3\n 4"
print(repr(test_str))  # '1 2\t 3\n 4'

# exercises
# shout
fname = input("Enter a file name: ")

try:
  fhand = open(f"./src/{fname}", "r")
except:
  print(f"File {fname} doesn't exists")
  quit()

for line in fhand:
  line = line.strip().upper()
  print(line)

fhand.close()

# avg d spam
fname = input("Enter a file name: ")

try:
  file_hand = open(f"./src/{fname}", "r")
except:
  print(f"File {fname} doesn't exist")
  quit()

d_spam = []

for line in file_hand:
  line = line.strip()
  if line.find("X-DSPAM-Confidence:") == -1: continue

  try:
    flo_num = float(line[20:])
  except:
    print("Conversion to float failed")
    quit()

  # print(flo_num, type(flo_num))
  d_spam.append(flo_num)

d_spam_avg = sum(d_spam) / len(d_spam)

print(f"Average DSpam Confidence: {d_spam_avg}")

# easter egg
file_name = input("Enter file name: ")

if file_name == "na na boo boo":
  print("NA NA BOO BOO TO YOU - You have been punk'd!")
  quit()

try:
  file_handle = open(f"./src/{file_name}", "r")
except:
  print(f"{file_name} cannot be opened")
  quit()

count = 0
for line in file_handle:
  line = line.strip()
  if line.startswith("Subject:"): 
    # print(line.lower())
    count += 1

print(f"{count} subject lines in {file_name}")