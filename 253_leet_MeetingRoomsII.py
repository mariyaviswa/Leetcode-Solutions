"""
253. Meeting Rooms II
---------------------

Given an array of meeting time interval objects consisting of start and end times
[[start_1,end_1],[start_2,end_2],...] (start_i < end_i), find the minimum number of days required
to schedule all meetings without any conflicts.

Example 1:
---------
Input: intervals = [(0,40),(5,10),(15,20)]

Output: 2
Explanation:
day1: (0,40)
day2: (5,10),(15,20)

Example 2:
----------
Input: intervals = [(4,9)]

Output: 1
Note:

(0,8),(8,10) is not considered a conflict at 8
"""

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
# catch-up : What is the question tells us the minimum number of rooms required that means the maximum of overlapping


def minMeetingRooms(intervals):
    # Time Complexity - O(n logn)
    # Space Complexity - O(n)
    start = sorted([i.start for i in intervals])
    end = sorted([i.end for i in intervals])

    s = 0
    e = 0
    res = meet = 0
    while s < len(start):
        if start[s] < end[e]:  # if the start is less than the end then this meeting is going on
            s += 1
            meet += 1
        else:  # else the meeting just got end
            e += 1
            meet -= 1
        res = max(meet, res)  # maximum overlapping count ( This tells us what is the minimum rooms required)
    return res


"""
min_heap solution
-----------------
        intervals.sort(key = lambda x : x.start)

        min_heap = []

        for interval in intervals:
            if min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)

            heapq.heappush(min_heap, interval.end)

        return len(min_heap)
"""
