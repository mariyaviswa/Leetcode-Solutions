"""
2762. Continuous Subarrays
--------------------------
problem link - https://leetcode.com/problems/continuous-subarrays/

You are given a 0-indexed integer array nums. A subarray of nums is called continuous if:

Let i, i + 1, ..., j be the indices in the subarray. Then, for each pair of indices i <= i1, i2 <= j, 0 <= |nums[i1] - nums[i2]| <= 2.
Return the total number of continuous subarrays.

A subarray is a contiguous non-empty sequence of elements within an array.



Example 1:
---------
Input: nums = [5,4,2,4]
Output: 8
Explanation:
Continuous subarray of size 1: [5], [4], [2], [4].
Continuous subarray of size 2: [5,4], [4,2], [2,4].
Continuous subarray of size 3: [4,2,4].
There are no subarrays of size 4.
Total continuous subarrays = 4 + 3 + 1 = 8.
It can be shown that there are no more continuous subarrays.


Example 2:
----------
Input: nums = [1,2,3]
Output: 6
Explanation:
Continuous subarray of size 1: [1], [2], [3].
Continuous subarray of size 2: [1,2], [2,3].
Continuous subarray of size 3: [1,2,3].
Total continuous subarrays = 3 + 2 + 1 = 6.


Constraints:
-----------
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
"""
from sortedcontainers import SortedList


def continuousSubarrays(nums):
    # Sliding-window
    # Time Complexity - O(n * log(n))
    # Space Complexity - O(n)
    l = 0
    sorted_window = SortedList()
    res = 0

    for i in range(len(nums)):
        sorted_window.add(nums[i])

        while sorted_window[-1] - sorted_window[0] > 2:  # keep tracking the window
            sorted_window.remove(nums[l])
            l += 1
        res += i - l + 1
    return res


arr = list(map(int, input().strip().split()))
ans = continuousSubarrays(arr)
print("Total Subarrays: ", ans)


"""
Using Hash map (Same approach as above)
--------------
def continuousSubarrays(self, nums: List[int]) -> int:
        # Sliding-window
        # Time Complexity - O(n * log(n))
        #Space Complexity - O(n)
        l = 0
        sub_map = {}
        res = 0

        for i in range(len(nums)):
            sub_map[nums[i]] = sub_map.get(nums[i], 0) + 1

            while max(sub_map) - min(sub_map) > 2:
                sub_map[nums[l]] -= 1
                if sub_map[nums[l]] == 0:
                    del sub_map[nums[l]]
                l += 1
            res += i - l + 1
        return res
"""

