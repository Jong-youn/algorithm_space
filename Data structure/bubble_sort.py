# 버블 정렬

import timeit
from icecream import ic

numbers1 = [7, 9, 1, 2, 10, 5, 6, 14, 90, 3]
numbers2 = [1, 2, 3, 5, 6, 7, 9, 10, 14, 90]

def bubble(nums):
    length = len(nums)
    for i in range(length-1):
        change = False
        for j in range(length-i-1):
            if nums[j] > nums[j+1]:
                change = True
                nums[j], nums[j+1] = nums[j+1], nums[j]
        if not change:
            return nums
    return nums

startTime = timeit.default_timer()
print(bubble(numbers1))
endTime = timeit.default_timer()
print(f"{endTime - startTime} 초 소요")

startTime = timeit.default_timer()
print(bubble(numbers2))
endTime = timeit.default_timer()
print(f"{endTime - startTime} 초 소요")