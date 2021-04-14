# 버블 정렬
numbers = [7, 9, 1, 2, 10, 5, 6, 14, 90, 3]

def bubble(nums):
    length = len(nums)
    for i in range(length-1):
        for j in range(length-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

print(bubble(numbers))