"""
739. Daily Temperatures
-----------------------

problem link - https://leetcode.com/problems/daily-temperatures/

Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:
---------
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
---------
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
---------
Input: temperatures = [30,60,90]
Output: [1,1,0]
"""


def dailyTemperatures(temperatures: list[int]) -> list[int]:
    # Time Complexity - O(n)
    # Space Complexity - O(n)
    n = len(temperatures)
    res = [0] * n  # set default value as 0
    stack = []  # [temp, idx] --> Monotonic Decreasing stack

    for i in range(n - 1, -1, -1):
        # Update for each index the greater value than this (very near value)
        if stack and temperatures[i] >= stack[-1][0]:
            while stack and temperatures[i] >= stack[-1][0]:
                stack.pop()

        if stack:
            res[i] += (stack[-1][1] - i)
        stack.append([temperatures[i], i])
    return res


nums = list(map(int, input().rstrip().split()))
ans = dailyTemperatures(nums)
print("Result: ", ans)
