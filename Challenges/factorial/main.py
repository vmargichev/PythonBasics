def factorial(num):
    print(num)
    factorial_result = 1
    while(num > 0):
        factorial_result = factorial_result * num
        num -= 1
    return factorial_result