# queue FIFO

# square a list
def sqr(nums):
    result = []
    while len(nums) > 0:
        x = nums.pop(0)
        result.append(x ** 2)
    return result


nums = [1, 2, 3, 4]
print(sqr(nums))
