# Challenge. we recieve an Array = [1, 2, 3, 4, 5, 6] and a sum. ex 8
# We need to find two numbers in the array that equals to the sum. Can not use same index value twice
# But can use same numbers. for example [6,4,3,1,4,6] is true cause there are two 4

array = [6,4,3,2,1,7]
sum = 9


# This solution takes lot of time O(n^2), because of the nested loops, which is not good
# but space complexity is O(1), we do not create new variables.
def hasPairWhithSum(array, sum):
    for i in range(len(array)):
        for j in range(len(array)):
            if (array[i] + array[j]) == sum and i != j:
                print("i ", array[i], "J ", array[j])
                return True
    return False


# print(hasPairWhithSum(array, sum))

# Better solution is to take a compliment of each element.
# example. array = [6,4,3,2,1,7]. 6 compliment would be 3 casue sum(9) - 6 = 3 and we save the compilment to new array
# if we have seen the compliment before we return true.
# SO in this case if the sum is 9 and compliment of 6 is 3 and 3 is in the array we return true
def hasPairWhithSum2(array, sum):
    # This solution is faster O(n), because we only use one for loop,
    # But space complexity is O(n) because we crete new array from the provided array so memory might become an issue.
    compliments = []
    for i in range(len(array)):
        if array[i] in compliments:
            return True
        else:
            compliments.append(sum - array[i])
    return False

print(hasPairWhithSum2(array, sum))
