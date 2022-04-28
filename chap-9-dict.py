from string import punctuation, digits

# highest word count program
fname = input("Enter a file name: ")

if fname == "q": quit()

try:
  fhandle = open(f"./src/{fname}", "r")
except:
  print("file does not exists")
  quit()

word_frequency = dict()

for line in fhandle:
  line = line.strip().lower()
  omit_list = [punctuation, digits]

  for omit in omit_list:
   line = line.translate(line.maketrans("", "", omit))

  line = line.split()

  for word in line:
    # understanding this is important
    word_frequency[word] = word_frequency.get(word, 0) + 1

# to find the word with highest frequency
hicount = None
hiword = None

word_trups = word_frequency.items()

for key, value in word_trups:
  if hicount is None or hicount < value:
    hicount = value
    hiword = key

# sort in reverse, highest first
sorted_words = sorted(word_trups, key=lambda x: x[1], reverse=True)

print(sorted_words)

print(f"The word '{hiword}' is used {hicount}")

fhandle.close()

# ex 1
try:
  file_handle = open("./src/words.txt", "r")
except:
  print("can't read file")
  quit()

all_words = {}

for line in file_handle:
  words_list = line.strip().split()
  for word in words_list:
    all_words[word] = all_words.get(word)

print("the" in all_words)  # True
print("office" in all_words)  # False

file_handle.close()

# histogram
word = "brontosaurus"
d = dict()
# basics
for char in word:
  if char not in d:
    d[char] = 1
  else:
    d[char] += 1

print(d)

# if d[char] exists get the value, else set the default as 0
for char in word:
  d[char] = d.get(char, 0) + 1

print(d)

# exercies
# day of the week counter
fname = input("Enter a file name: ")
try:
  fhandle = open(f"./src/{fname}", "r")
except:
  print("file read error")
  quit()

weekdays = {}

for line in fhandle:
  line = line.strip()

  if line.startswith("From") and not line.startswith("From:"):
    line = line.split()

    weekdays[line[2]] = weekdays.get(line[2], 0) + 1

# print(sorted(list(weekdays.items()), key=lambda x: x[1], reverse=True))
print(weekdays)

fhandle.close()

# email counter
fname = input("Enter a file name: ")
try:
  fhandle = open(f"./src/{fname}", "r")
except:
  print("file read error")
  quit()

emails = {}

for line in fhandle:
  line = line.strip()

  if line.startswith("From") and not line.startswith("From:"):
    line = line.split()

    emails[line[1]] = emails.get(line[1], 0) + 1


print(emails)

# Find the highest email sender
emails_tup = emails.items()

hicount = None
hisender = None

for key, val in emails_tup:
  if hicount is None or hicount < val:
    hicount = val
    hisender = key

print(hisender, hicount)

# Find the highest records of domain name
domains = {}

for key, val in emails_tup:
  domain = key.split("@")[1]

  domains[domain] = domains.get(domain, 0) + val

print(domains)

fhandle.close()