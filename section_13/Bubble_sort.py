numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


# Own version. Whit loop because I am a dummy dum dum.
def bubble_sort(array):
    i = 0
    total_loops = 0
    length = len(array) - 1
    # When length is 1 then it should have sorted the array
    while length != 1:
        total_loops += 1
        # Reset the index to the beginning and reduce the length when loop is finished
        # This way we don't have to go through already sorted items.
        if i >= length:
            length -= 1
            i = 0
        print(array[i], array[i + 1])
        print(array)
        # Make them moves like a jagger
        if array[i] > array[i + 1]:
            array[i + 1], array[i] = array[i], array[i + 1]
        i += 1
    print("Total loops done ", total_loops)


bubble_sort(numbers)
print(numbers)

# Example version
