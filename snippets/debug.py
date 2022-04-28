# debugging tips
test_str = "1 2\t 3\n 4"
print(repr(test_str))  # '1 2\t 3\n 4'

nums = [11, 27, 39, [2, 4], 50]

# isinstance() is important
for i in range(len(nums)):
  if isinstance(nums[i], list):
    print("found a nested list", nums[i])
    continue

  nums[i] *= 2

print(nums)

# use dir() to find methods
l = []
print(dir(l))

# Use help
help("modules")