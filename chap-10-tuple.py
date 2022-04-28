# Tuples are like list, but are immutable data-structures
t = ("harry", 76)

# Sorting value-key pairs using tuples
d = {"a": 10, "b": 1, "c": 22}
tmp = []

for (k, v) in d.items():
  tmp.append((v, k))

tmp = sorted(tmp, reverse=True)
print(tmp)

# Shorter version of sorting
dct = {"a": 10, "b": 1, "c": 22}
# This is a list of tuples (v, k)
lst = sorted([(v, k) for k, v in dct.items()], reverse=True)
print(lst)

# Another way
lst2 = sorted(list(dct.items()), key=lambda x: x[1], reverse=True)
print(lst2)

# You can't modify a tuple, but replace one tuple with another
tup = ("A", "b", "c", "d")
tup = ("a",) + tup[1:]
print(tup)

txt = 'but soft what light in yonder window breaks'
words = txt.split()

word_lst = []
for w in words:
  word_lst.append((len(w), w))

word_lst.sort(reverse=True)
# print(word_lst)

max_words = []

for (l, word) in word_lst:
  max_words.append(word)

print(max_words)

t = (20, 50)
# Kinda like destructuring in JS
x, y = t

# x = t[0]  # 20
# y = t[1]  # 50

print(x, type(x))
print(y, type(y))

email = "viknegi0@gmail.com"
uname, domain = email.split("@")

print(uname, domain)

# Because tuples are hashable (immutable), we can use them as keys to use in a dictionary
# A tuple as a key is called a composite key
phone_dir = {}
# phone_dir[last_name, first_name] = phone_number
phone_dir["negi", "vikram"] = "8850926613"

print(phone_dir) # {("negi", "vikram"): "8850926613"}

for last, first in phone_dir:
  print(f"{first.capitalize()} {last.capitalize()} +91-{ phone_dir[last, first]}")

# If you are passing a sequence as an argument to a function, using tuples reduces the potential for unexpected behavior due to aliasing.

# exercises
file_name = input("Enter file name: ")

try:
  fhandle = open(f"./src/{file_name}", "r")
except:
  print("file open err")
  quit()

emails = {}

for line in fhandle:
  line = line.strip()
  
  if line.startswith("From") and not line.startswith("From:"):
    words = line.split()
    emails[words[1]] = emails.get(words[1], 0) + 1

lst = []
for email, count in emails.items():
  lst.append((count, email))

lst.sort(reverse=True)

# lst = sorted([(v, k) for k, v in emails.items()], reverse=True)


fhandle.close()

print(lst[0][1], lst[0][0])

# count hours in asc
file_name = input("Enter file name: ")

try:
  fhandle = open(f"./src/{file_name}", "r")
except:
  print("file open err")
  quit()

hours = {}

for line in fhandle:
  line = line.strip()
  
  if line.startswith("From") and not line.startswith("From:"):
    words = line.split()
    time_hours = words[5].split(":")

    hours[time_hours[0]] = hours.get(time_hours[0], 0) + 1

hours_list = list(hours.items())

hours_list.sort()

# Makes it look so easy
lst = sorted([(v, k) for k, v in hours.items()], reverse=True)

for hr, c in hours_list:
  print(hr, c)


fhandle.close()

# print(hours_list)

# count alpha a-z
from string import punctuation, digits

file_name = input("Enter file name: ")

try:
  fhandle = open(f"./src/{file_name}", "r")
except:
  print("file open err")
  quit()

omit_list = [punctuation, digits, " ", "\\", "\t"]

words_dict = {}

for line in fhandle:
  line = line.strip().lower()

  for omit in omit_list:
    line = line.translate(line.maketrans("", "", omit))

  for word in line:
    words_dict[word] = words_dict.get(word, 0) + 1

if len(words_dict) != 26: 
  print(f"{len(words_dict)} alphabets only")

wordF= []

for alpha, count in words_dict.items():
  wordF.append((count, alpha))

wordF.sort(reverse=True)

# # Prints alphabet-frequency
for fTup in wordF:
  print(fTup[1], fTup[0])

total = 0

for fTup in wordF:
  total += fTup[0]

search_for = input("Enter an alphabet: ")

try:
  alphabet_count = words_dict[f"{search_for}"]
  alpha_percent = round(alphabet_count / total * 100, 2)
  print(f"{search_for} was used {alphabet_count} times")
  print(f"{alpha_percent}% of the entire text")
except:
  print("invalid alphabet")
  quit()