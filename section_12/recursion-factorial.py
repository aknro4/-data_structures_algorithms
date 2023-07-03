answer_1 = 1


def find_factorial_recursive(number):
    global answer_1
    answer_1 *= number
    number -= 1
    if number == 0:
        return answer_1
    return find_factorial_recursive(number)


# Loops
def find_factorial_iterative(number):
    answer_2 = 1
    while number != 0:
        answer_2 *= number
        number -= 1
    return answer_2


print(find_factorial_recursive(5))
print(find_factorial_iterative(5))
