def merge(left, right):
  arr = []
  while len(left) and len(right):
    # ascending order
    if left[0] < right[0]:
      arr.append(left.pop(0))
    else:
      arr.append(right.pop(0))

  return arr + left + right

def mergeSort(main_arr):
  half = len(main_arr) // 2

  if len(main_arr) == 1: return main_arr

  left = main_arr[:half]
  right = main_arr[half:]
  # recursion
  return merge(mergeSort(left), mergeSort(right))

test_arr = [2, 4, 5, 1, 9, 7, 57, 18, 39 ,291, 195, 12, 50, 82, 1, 51, 52, 69, 510]

print(mergeSort(test_arr))