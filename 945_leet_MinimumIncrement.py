"""
945. Minimum Increment to Make Array Unique
-------------------------------------------

You are given an integer array nums. In one move, you can pick an index i where 0 <= i < nums.length and increment nums[i] by 1.
Return the minimum number of moves to make every value in nums unique.

The test cases are generated so that the answer fits in a 32-bit integer.

Example 1:
---------
Input: nums = [1,2,2]
Output: 1
Explanation: After 1 move, the array could be [1, 2, 3].

Example 2:
----------
Input: nums = [3,2,1,2,1,7]
Output: 6
Explanation: After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.
"""


def minIncrementForUnique(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Time complexity - O(n logn)
    # space complexity - O(1)
    nums.sort()
    count = 0
    for num in range(1, len(nums)):
        if nums[num - 1] == nums[num]:  # check with prev element if same then increment
            nums[num] += 1
            count += 1
        elif nums[num] < nums[num - 1]:  # if less than prev element
            count += abs(nums[num - 1] - nums[num]) + 1
            nums[num] = nums[num - 1] + 1
    return count


Nums = list(map(int, input().rstrip().split()))
print(minIncrementForUnique(Nums))
