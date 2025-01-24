"""
523. Continuous Subarray Sum
----------------------------

Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.
A good subarray is a subarray where:
its length is at least two, and
the sum of the elements of the subarray is a multiple of k.

Note that:
---------
A subarray is a contiguous part of the array.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

Example 1:
---------
Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.

Example 2:
----------
Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is a continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.

Example 3:
----------
Input: nums = [23,2,6,4,7], k = 13
Output: false

"""


def checkSubarraySum(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    """
    if len(nums) < 2:
        return False
    if sum(nums) % k == 0:
        return True
    else:
        for i in range(0, len(nums)-1):
            Sum = 0
            count = 0
            for j in range(i, len(nums)):
                Sum += nums[j]
                count += 1
                if count >= 2 and (Sum == 0 or Sum >= k):
                    if Sum % k == 0:
                        return True
        return False
    """
    # why we add this from starting in dictionary
    """
    We add {0 : -1} in dict not to handle case where 1st element is divisible by k. 
    We add it to handle case where subarray starting from 0 is divisible by k.
    Because if the first element is divisible by k the it check in hash map already {0:-1} is there so now we want add {0:0}
    but it check condition in below code (0-(-1)) = 1 not greater than 1 (i,e 1==1)
    so for this we add this in starting.
    
    Here [23, 2, 4, 6, 7], k =6
    dict = {0:-1}
    add val from starting 
    1st -> 23 % 6 = 5 , add it to dict {5:0}
    2nd -> (23+2) % 6 = 1, add it to dict {1:1}
    3rd -> (23+2+4) % 6 = 5, add it to dict {5:2}
    Here we can see already 5 is there, so it won't add to dict further it check difference between index's (2-0 = 2 > 1). So return True
    """
    dictionary = {0: -1}
    Sum = 0
    for index, num in enumerate(nums):
        Sum += num
        remain = Sum % k
        if remain not in dictionary:
            dictionary[remain] = index
        elif index - dictionary[remain] > 1:
            return True
    return False


Nums = list(map(int, input().rstrip().split()))
K = int(input())
print(checkSubarraySum(Nums, K))
