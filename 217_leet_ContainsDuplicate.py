"""
217. Contains Duplicate
-----------------------

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
---------
Input: nums = [1,2,3,1]
Output: true

Example 2:
----------
Input: nums = [1,2,3,4]
Output: false

Example 3:
----------
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""


def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    Hash_map = {}
    for num in nums:
        if num in Hash_map:
            return True
        else:
            Hash_map[num] = 1
    return False


nums_list = list(map(int, input().rstrip().split()))
print(containsDuplicate(nums_list))
