from math import factorial as fact


def factorial(n):
    p = 1
    for i in range(2, n + 1):
        p *= i

    print("my factorial")
    return p
