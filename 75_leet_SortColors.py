"""
75. Sort Colors
---------------

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent,
with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.

Example 1:
---------
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
---------
Input: nums = [2,0,1]
Output: [0,1,2]
"""


def sortColors(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    """
    # another solution 
    zeros = 0
    ones = 0
    twos = 0
    for num in nums:
        if num == 0:
            zeros += 1
        elif num == 1:
            ones += 1
        else:
            twos += 1
    for i in range(0, zeros):
        nums[i] = 0
    for j in range(zeros, zeros+ones):
        nums[j] = 1
    for k in range(zeros+ones, zeros+ones+twos):
        nums[k] = 2 
    """
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]


numbers = list(map(int, input().rstrip().split()))
print(sortColors(numbers))
