numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def insertion_sort(array):
    length = len(array)
    for i in range(length):
        if array[i] < array[0]:
            # Move the number to the first position
            array.insert(0, array.pop(i))
        else:
            # Only sort numbers smaller than the number on the left of it
            # This is the part of insertion sort that makes it fast if the array is almost sorted
            if array[i] < array[i - 1]:
                # Find where the number should go
                for j in range(1, i):
                    if array[j - 1] <= array[i] < array[j]:
                        # Move the number to the right spot
                        array.insert(j, array.pop(i))
                        break


insertion_sort(numbers)
print(numbers)
