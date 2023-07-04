numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def selection_sort(array):
    # Increase the starting index after smallest value gets sorted to the beginning
    start = 0
    length = len(array) - 1
    # Current index
    i = 0
    # Smallest value index, could use better naming like small instead of j
    j = 0
    while start != length:
        if i > length:
            # starting index gets replaced by the smallest value index.
            # And starting index to the smallest value index.
            array[start], array[j] = array[j], array[start]
            # print(array)
            # Increase the starting index
            start += 1

            i = start
            j = start
        # print(array[j], array[i])
        # save the index to j if smaller value has been found
        if array[j] > array[i]:
            j = i
            # print("New smallest value ", array[j])
        i += 1


selection_sort(numbers)
print(numbers)
