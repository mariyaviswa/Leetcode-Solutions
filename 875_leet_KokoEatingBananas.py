"""
875. Koko Eating Bananas
------------------------

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas.
The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile.
If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.



Example 1:
----------
Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:
---------
Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:
----------
Input: piles = [30,11,23,4,20], h = 6
Output: 23
"""

import math


def minEatingSpeed(piles: list[int], h: int) -> int:
    # Time Complexity - O(N * Log(MAX(piles)))
    # Space Complexity - O(1)
    l, r = 1, max(piles)
    res = r

    while l <= r:
        mid = (l + r) // 2
        tot_hour = 0
        for p in piles:
            tot_hour += math.ceil(p / mid)
        if tot_hour <= h:
            res = min(res, mid)
            r = mid - 1
        else:
            l = mid + 1
    return res


nums = list(map(int, input().split()))
hour = int(input())
ans = minEatingSpeed(nums, hour)
print("Minimum rate: ", ans)