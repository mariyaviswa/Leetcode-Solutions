"""
34. Find First and Last Position of Element in Sorted Array
-----------------------------------------------------------

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Example 1:
----------
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
----------
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
----------
Input: nums = [], target = 0
Output: [-1,-1]
"""


def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    if len(nums) == 0 or target not in nums:
        return [-1, -1]
    if target in nums:
        temp_index = 0
        flag = False
        left = 0
        right = len(nums) - 1
        # Using binary search find the index position of target - Time complexity O(log n)
        while left <= right:
            midpoint = (left + right) // 2
            if nums[midpoint] == target:
                temp_index = midpoint  # store the index value  in temp variable
                flag = True
                break
            elif nums[midpoint] < target:
                left = midpoint + 1
            else:
                right = midpoint - 1
    start = temp_index
    end = temp_index
    while start > 0:  # Then find the accurate starting position
        if nums[start - 1] == target:
            start -= 1
        else:
            break
    while end < len(nums) - 1:  # find the ending position
        if nums[end + 1] == target:
            end += 1
        else:
            break
    return [start, end]


Nums = list(map(int, input().rstrip().split()))
Target = int(input())
print(searchRange(Nums, Target))