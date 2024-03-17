# three ways to find fibonacci number

# recursion
def fib1(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fib1(n - 1) + fib1(n - 2)


print(fib1(20))


# notebook
def fib2(n, nb={}):
    if n in nb:
        return nb[n]
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    result = fib2(n - 1, nb) + fib2(n - 2, nb)
    nb[n] = result
    return result


print(fib2(10, {}))


# iterative
def fib3(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a


print(fib3(10))
