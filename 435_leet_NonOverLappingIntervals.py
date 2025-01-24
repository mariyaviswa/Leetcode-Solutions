"""
435. Non-overlapping Intervals
------------------------------

problem link - https://leetcode.com/problems/non-overlapping-intervals/

Given an array of intervals  where intervals[i] = [starti, endi],
return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.



Example 1:
---------
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Example 2:
----------
Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

Example 3:
---------
Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

"""


def eraseOverlapIntervals(intervals):
    # Time Complexity - O(n logn)
    # Space Complexity - O(1) or O(n)

    intervals.sort()

    end = intervals[0][1]
    cnt = 0
    for i in range(1, len(intervals)):
        if intervals[i][0] < end:
            end = min(intervals[i][1], end)
            cnt += 1
        else:
            end = intervals[i][1]
    return cnt


interval = []
n = int(input())

for i in range(n):
    inp = list(map(int, input().rstrip().split()))
    interval.append(inp)
res = eraseOverlapIntervals(interval)
print("The minimum number of Intervals to remove is: ", res)
