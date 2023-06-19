
def test(array1, array2):
    for i in range(len(array1)):
        if array1[i] in array2:
            return True
    return False

array1 = ['a','b','c','d','e',]
array2 = ['x','a','ö','q','j']
print(test(array1, array2))