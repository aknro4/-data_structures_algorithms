numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def quick_sort(array, left, right):
    if left < right:
        # Partition the array and get the index of the pivot
        pivot_index = partition(array, left, right)

        # Recursively sort the sub lists
        quick_sort(array, left, pivot_index - 1)
        quick_sort(array, pivot_index + 1, right)


# Responsible for partitioning the array into two sublist, based on the pivot element.
def partition(array, left, right):
    # Right most element in array as the pivot
    pivot = array[right]
    # Keeps track of the last element in the sub list.
    i = left - 1
    print(pivot)
    print(array)

    for j in range(left, right):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[right] = array[right], array[i + 1]
    return i + 1


# Select first and last index as 2nd and 3rd parameters
quick_sort(numbers, 0, len(numbers) - 1)
print(numbers)
