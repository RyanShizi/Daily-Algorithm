f = 10


def recursion(f):
    assert f >= 0
    if f == 1:
        return 1
    else:
        return f + recursion(f - 1)


result = recursion(f)
print(result)
