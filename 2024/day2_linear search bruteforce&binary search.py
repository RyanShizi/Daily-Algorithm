import time

n = 678223072849


def linearSearch(n):
    for i in range(1, n):
        if i ** 2 == n:
            return i


start_time = time.perf_counter()
result = linearSearch(n)
print(result)
end_time = time.perf_counter()

print("---------------------")

m = 678223072849
low = 0
high = m


def binarySearch(m):
    while low <= high:
        mid = (low + high) // 2
        if mid ** 2 == m:
            return mid
        if mid ** 2 > m:
            high = mid - 1
        else:
            low = mid + 1


start_time2 = time.perf_counter()
result = linearSearch(m)
print(result)
end_time2 = time.perf_counter()

print(((end_time - start_time) * 1000))
print(((end_time2 - start_time2) * 1000))
