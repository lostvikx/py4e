# Check the wikipedia page for Letter Frequencies in texts

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