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