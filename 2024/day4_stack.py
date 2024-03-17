# stack FILO

# reverse a list
def rev(nums):
    result = []
    while len(nums) > 0:
        x = nums.pop()
        result.append(x)
    return result


nums = [1, 2, 3, 4]
print(rev(nums))