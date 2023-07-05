numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

# Yep this is really hard to fully understand
def merge_sort(array):
    if len(array) == 1:
        # print("Array length was 1")
        return array

    #  Split Array in into right and left
    middle = len(array) // 2
    left_half = array[:middle]
    right_half = array[middle:]

    # print("Left half: ", left_half)
    # print("Right half: ", right_half)

    # Recursively split arrays into left and right half's
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # My brain is fucked
    return merge(
        merge_sort(left_half),
        merge_sort(right_half)
    )


def merge(left, right):
    merged = []
    left_index = right_index = 0
    # print("Merging")
    # Compare elements from left to right and add the smaller element to the merged array.
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            # print("Left was smaller ", left[left_index], " than right ", right[right_index])
            merged.append(left[left_index])
            left_index += 1
        else:
            # print("Left was larger ", left[left_index], " than right ", right[right_index])
            merged.append(right[right_index])
            right_index += 1

    # Add the remaining elements to the merged array if any
    while left_index < len(left):
        # print("Remaining left elements: ", left[left_index])
        merged.append(left[left_index])
        left_index += 1
        # print("Merged list ", merged)

    while right_index < len(right):
        # print("Remaining right elements: ", right[right_index])
        merged.append(right[right_index])
        right_index += 1
        # print("Merged list ", merged)

    print(left, right)

    return merged


answer = merge_sort(numbers)
print(answer)
