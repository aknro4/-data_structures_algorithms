# Given a number N return the index value of the Fibonacci sequence, where the sequence is:

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 ...
# the pattern of the sequence is that each value is the sum of the 2 previous values, that means that for N=5 → 2+3

# For example: fibonacciRecursive(6) should return 8
counter = 2
first_num = 0
last_num = 1


def fibonacci_iterative(n):
    global first_num, last_num, counter
    result = first_num + last_num
    if counter == n:
        return result
    first_num = last_num
    last_num = result
    counter += 1
    return fibonacci_iterative(n)


print(fibonacci_iterative(3))


def fibonacci_recursive(n):
    counter_1 = 2
    first_number = 0
    last_number = 1
    while True:
        result = first_number + last_number
        if counter_1 == n:
            return result
        first_number = last_number
        last_number = result
        counter_1 += 1


print(fibonacci_recursive(3))
