def mergeSortedArrays(arr1, arr2):
    sortedArrays = []
    # If we can use sort() funtion, then... we can do it simply like this
    # for i in arr1:
    #     sortedArrays.append(i)
    # for j in arr2:
    #     sortedArrays.append(j)
    # sortedArrays.sort()

    # if cant use sort function. Then compare each value whit each other and insert the one that is greater.
    # We then need to use nested looping.
    # Very specific implementation, mostly works only if arr1 length > arr2 length
    # for i in arr1:
    #     for j in arr2:
    #         print("Comparing i " , i, "and j ", j, "Values")
    #         if i > j:
    #             sortedArrays.append(j)
    #         Break when i is smaller than j so we can compare next i value to j
    #         elif i < j:
    #             sortedArrays.append(i)
    #             break
    #         else:
    #             sortedArrays.append(j)
    #             arr2.remove(j)
    #
    #     print("sortedArrays ",sortedArrays)

    # Same consept as above, but whit while loop. and does not matter which array is longest.
    while True:
        if len(arr1) == 0:
            # If one of other arrays has more than 2 remaining elements left we loop it through and append them.
            for i in arr2:
                sortedArrays.append(i)
            return sortedArrays
        elif len(arr2) == 0:
            for i in arr1:
                sortedArrays.append(i)
            return sortedArrays

        arr1Item = arr1[0]
        arr2Item = arr2[0]

        print("Comparing arr1Item ", arr1Item, " to arr2Item ", arr2Item)

        if arr1Item > arr2Item:
            sortedArrays.append(arr2Item)
            arr2.remove(arr2Item)
        elif arr1Item < arr2Item:
            sortedArrays.append(arr1Item)
            arr1.remove(arr1Item)
        # if values are equal
        else:
            sortedArrays.append(arr1Item)
            arr2.remove(arr2Item)
    # FOr other solutions
    return sortedArrays




print(mergeSortedArrays([0,3,4,31],[4,6,30]))

