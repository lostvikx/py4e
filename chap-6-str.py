user_name = "vikram"
print(user_name[len(user_name) - 1])  # m
print(user_name[-1])  # m

def rev_name(name):
  i = len(name) - 1
  result = ""

  while i >= 0:
    result += name[i]
    i -= 1

  return result

rev_user_name = rev_name(user_name)
print(rev_user_name)

# similar to slice() is js
test_str = "markiv"
print(rev_name(test_str[3:]))

greet = "Hello, World!"
print("L" + greet[1:])

def count(word, letter):
  result = 0
  for i in word:
    if i == letter: result += 1
  
  return f"{word.capitalize()} has {result} '{letter}'"

print(count("adriana", "a"))
print("adriana".count("a"))

print("x" in "alexis")

# format operator
dogo_name = "jacky"
dogs = 10
print("I saw %d dogs running wild, one of them was named %s." % (dogs, dogo_name.capitalize()))

# exercise
test_str = 'X-DSPAM-Confidence:0.8475'
start = test_str.find(":")
try:
  print(float(test_str[start+1:]))
except:
  print("coundn't convert to float")
  quit()