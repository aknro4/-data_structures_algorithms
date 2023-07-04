numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

def merge_sort (array):
  if len(array) == 1:
    return array

  #  Split Array in into right and left

  return merge(
    merge_sort(left),
    merge_sort(right)
  )


def merge(left, right):


answer = merge_sort(numbers)
print(answer)