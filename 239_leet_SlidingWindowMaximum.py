"""
239. Sliding Window Maximum
---------------------------

problem link - https://leetcode.com/problems/sliding-window-maximum/

You are given an array of integers nums, there is a sliding window of size k which is moving
from the very left of the array to the very right.
You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:
---------
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
                Window position                Max
                ---------------               -----
                [1  3  -1] -3  5  3  6  7       3

                 1 [3  -1  -3] 5  3  6  7       3

                 1  3 [-1  -3  5] 3  6  7       5

                 1  3  -1 [-3  5  3] 6  7       5

                 1  3  -1  -3 [5  3  6] 7       6

                 1  3  -1  -3  5 [3  6  7]      7

Example 2:
----------
Input: nums = [1], k = 1
Output: [1]
"""

import collections


def maxSlidingWindow(nums, k):
    # Time Complexity - O(n)
    # Space Complexity - O(n)

    # Monotonic Decreasing Queue
    track = collections.deque()
    st = 0
    ed = 0

    for idx, num in enumerate(nums):
        if track and num > track[-1][0]:
            while track and num > track[-1][0]:
                track.pop()
        track.append([num, idx])
        ed = idx + 1  # update the end of window
        # Store the maximum for each window
        if ed - st == k:
            nums[st] = track[0][0]
            st += 1
        # Remove the index value if out of bound
        if track[0][1] < st:
            track.popleft()
    return nums[:st]


arr = list(map(int, input().rstrip().split()))
size = int(input())
res = maxSlidingWindow(arr, size)
print("Maximum of Each Window: ", res)