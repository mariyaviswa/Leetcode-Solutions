"""
Indexes of Subarray Sum
-----------------------

Given an array arr[] containing only non-negative integers,
your task is to find a continuous subarray (a contiguous sequence of elements)
whose sum equals a specified value target. You need to return the 1-based indices
of the leftmost and rightmost elements of this subarray. You need to find the first subarray whose sum is equal to the target.

Note: If no such array is possible then, return [-1].
-----

Examples:
--------
Input: arr[] = [1, 2, 3, 7, 5], target = 12
Output: [2, 4]
Explanation: The sum of elements from 2nd to 4th position is 12.

Input: arr[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], target = 15
Output: [1, 5]
Explanation: The sum of elements from 1st to 5th position is 15.

Input: arr[] = [5, 3, 4], target = 2
Output: [-1]
Explanation: There is no subarray with sum 2.
"""


def subarraySum(arr, target):
    # code here

    l = 0
    r = 0

    Sum = arr[l]

    while r < len(arr):
        if Sum == target:
            return [l + 1, r + 1]
        elif Sum < target:
            r += 1
            if r < len(arr): Sum += arr[r]
        else:
            Sum -= arr[l]
            l += 1
    return [-1]


nums = list(map(int, input().rstrip().split()))
k = int(input())
res = subarraySum(nums, k)
print("Subarray sum indices: ", res)
