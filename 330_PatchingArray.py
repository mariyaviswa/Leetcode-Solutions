"""
330. Patching Array
-------------------

Given a sorted integer array nums and an integer n, add/patch elements to the array such that any number in the range [1, n]
inclusive can be formed by the sum of some elements in the array.

Return the minimum number of patches required.

Example 1:
----------
Input: nums = [1,3], n = 6
Output: 1
Explanation:
Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
So we only need 1 patch.

Example 2:
----------
Input: nums = [1,5,10], n = 20
Output: 2
Explanation: The two patches can be [2, 4].
Example 3:

Input: nums = [1,2,2], n = 5
Output: 0

"""


def minPatches(nums, n):
    """
    :type nums: List[int]
    :type n: int
    :rtype: int
    """
    """
    Example
    -------
    [1,5,10] , n = 20
    sum = 0, index = 0
    0 < 3 and  1  <= 0+1,  yes,  sum = 1,       index = 1
    1 < 3 and  5  <= 1+1,  No,   sum = 1+(1+1)=3,  tot_patch = 1
    1 < 3 and  5  <= 3+1,  No,   sum = 2+(2+1)=5 , tot_patch = 2
    1 < 3 and  1  <= 5+1,  Yes,  sum = 10,      index = 2
    2 < 3 and  10 <= 10+1, Yes,  sum = 20
    stop.
    
    """
    tot_patch = 0
    Sum = 0
    index = 0
    while Sum < n:
        if index < len(nums) and nums[index] <= Sum + 1:
            Sum += nums[index]
            index += 1
        else:
            tot_patch += 1
            Sum += (Sum + 1)
    return tot_patch


numbers = list(map(int, input().rstrip().split()))
N = int(input())
print(minPatches(numbers, N))


