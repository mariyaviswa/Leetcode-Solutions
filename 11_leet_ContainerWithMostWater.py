"""
11. Container With Most Water
-----------------------------
problem link - https://leetcode.com/problems/container-with-most-water/

You are given an integer array height of length n. There are n vertical lines drawn such that
the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
----------
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
----------
Input: height = [1,1]
Output: 1
"""


def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    # Time Complexity - O(n)
    # Space Complexity - O(1)

    # Assign Two-pointer
    left = 0
    right = len(height) - 1
    max_water = 0  # for to store the max area
    while left < right:
        currMax = (right - left) * min(height[left], height[right])
        if height[left] < height[right]:  # find which pointer has low value then move the side
            left += 1
        else:  # else move right side
            right -= 1
        max_water = max(currMax, max_water)  # find the maximum area
    return max_water


container_heights = list(map(int, input().rstrip().split()))
print("Maximum Water level: ", maxArea(container_heights))
