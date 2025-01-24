"""
560. Subarray Sum Equals K
--------------------------

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.



Example 1:
----------
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
----------
Input: nums = [1,2,3], k = 3
Output: 2
"""


def subarraySum(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    # Time Complexity - O(n)
    # Space Complexity - O(n)
    sumCount = {0: 1}
    """
    why we add the default case {0 : 1}
    
    Think about it arr = [4, 1, 4], k = 4
    curr  counts
    {0 :   1, 
     4 :   1, here the starting element 4 , 4 - 4 == 0 is already in our map,  so that increase the res (by default we already put)
     5 :   1, 
     9 :   1} in that case 9 - 4 == 5 is already in our map, so that increase the res (by default we already put)
    """
    curr, res = 0, 0

    for i in range(0, len(nums)):
        curr += nums[i]
        if curr - k in sumCount:
            res += sumCount.get(curr - k, 0)
        sumCount[curr] = sumCount.get(curr, 0) + 1
    return res


Nums = list(map(int, input().rstrip().split()))
K = int(input())
print(f"Total Subarrays that sum equals {K}: ", subarraySum(Nums, K))