"""
Largest subarray of 0's and 1's
-------------------------------

This problem same as --> ** subarray sum equals k and ** longest subarray with sum k
                            ---------------------        ---------------------------

problem link - https://www.geeksforgeeks.org/problems/largest-subarray-of-0s-and-1s/1

Given an array arr of 0s and 1s. Find and return the length of the longest subarray with equal number of 0s and 1s.

Examples:
---------

Input: arr[] = [1, 0, 1, 1, 1, 0, 0]
Output: 6
Explanation: arr[1...6] is the longest subarray with three 0s and three 1s.

Input: arr[] = [0, 0, 1, 1, 0]
Output: 4
Explanation: arr[0...3] or arr[1...4] is the longest subarray with two 0s and two 1s.

Input: arr[] = [0]
Output: 0
Explanation: There is no subarray with an equal number of 0s and 1s.
"""


def maxLen(arr):
    # code here

    nums = {0: -1}

    Sum, maxLength = 0, 0
    for i in range(0, len(arr)):
        Sum += 1 if arr[i] == 1 else -1

        if Sum in nums:
            maxLength = max(maxLength, i - nums[Sum])
        else:
            nums[Sum] = i
    return maxLength


nums = list(map(int, input().split()))
res = maxLen(nums)
print("Maximum length of subarray: ", res)