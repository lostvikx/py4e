knights = {'gallahad': 'the pure', 'robin': 'the brave'}

# these do the same thing
for knight in knights.keys():
  print(knight, knights[knight])

# but, this looks more sophisticated (concise)
for knight, tag in knights.items():
  print(knight, tag)

# convert to list
# .items() doesn't return a list by default
knights_list = list(knights.items())
