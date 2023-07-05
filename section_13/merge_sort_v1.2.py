numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


# Coded top of my head.
def merge_sort(array):
    if len(array) == 1:
        return array

    # Split array
    middle = len(array) // 2
    left_half = array[middle:]
    right_half = array[:middle]

    # Recursive function
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(
        merge_sort(left_half),
        merge_sort(right_half)
    )


def merge(left, right):
    merged = []
    left_index = right_index = 0

    # Append smaller value into array
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Append left over values
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


answer = merge_sort(numbers)
print(answer)
