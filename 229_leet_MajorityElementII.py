"""
229. Majority Element II
------------------------

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Example 1:
---------
Input: nums = [3,2,3]
Output: [3]

Example 2:
---------
Input: nums = [1]
Output: [1]

Example 3:
---------
Input: nums = [1,2]
Output: [1,2]
"""


def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    size = int(len(nums) / 3)  # calculate the size
    dictionary = {}  # create an empty hash map
    for num in nums:
        if num in dictionary:  # if already the num in hash map increase its value by 1
            dictionary[num] += 1
        else:
            dictionary[num] = 1  # if not the assign value 1 to the num in hash map
    print(dictionary)
    majority = []  # create an empty list to append answers
    for key in dictionary:
        if dictionary[key] > size:  # if each key's value greater than size
            majority.append(key)
    return majority


Nums = list(map(int, input().rstrip().split()))
print(majorityElement(Nums))
