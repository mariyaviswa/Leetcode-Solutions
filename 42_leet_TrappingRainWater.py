"""
42. Trapping Rain Water
-----------------------

problem link -https://leetcode.com/problems/trapping-rain-water/

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.

Example 1:
---------

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
----------
Input: height = [4,2,0,3,2,5]
Output: 9

"""


def trap(height):
    # Time Complexity - O(n)
    # Space Complexity - O(1)
    if not height: return 0

    l = 0
    r = len(height) - 1
    res = 0

    maxLeft = height[l]
    maxRight = height[r]

    while l < r:
        if maxLeft < maxRight:  # No matter carry about the which is minimum i.e, (maxLeft, maxRight), this condition takes care of that
            l += 1
            maxLeft = max(maxLeft, height[l])  # Update the left max so far seen till this point
            res += maxLeft - height[l]
        else:
            r -= 1
            maxRight = max(maxRight, height[r])  # Update the left max so far seen till this point
            res += maxRight - height[r]
    return res


"""
Using extra spaces
-------------------

    Time Complexity - O(n)
    Space Complexity - O(n)
    maxLeft = [0] * len(height)
    maxRight = [0] * len(height)
    maxLeft[0] = height[0]
    maxRight[-1] = height[-1]

    for i in range(1, len(height)):
        maxLeft[i] = max(maxLeft[i-1], height[i])
    for j in range(len(height)-2, -1, -1):
        maxRight[j] = max(maxRight[j+1], height[j])
    
    res = 0
    for i in range(0, len(height)):
        res += min(maxLeft[i], maxRight[i]) - height[i]
    return res
"""

nums = list(map(int, input().split()))
ans = trap(nums)
print("Total trap water: ", ans)
