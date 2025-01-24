"""
Count the number of possible triangles
--------------------------------------

Given an integer array arr[]. Find the number of triangles that can be formed with three different array elements
as lengths of three sides of the triangle.

A triangle with three given sides is only possible if sum of any two sides is always greater than the third side.

Examples:
--------
Input: arr[] = [4, 6, 3, 7]
Output: 3
Explanation: There are three triangles possible [3, 4, 6], [4, 6, 7] and [3, 6, 7]. Note that [3, 4, 7] is not a possible triangle.

Input: arr[] = [10, 21, 22, 100, 101, 200, 300]
Output: 6
Explanation: There can be 6 possible triangles: [10, 21, 22], [21, 100, 101], [22, 100, 101],
[10, 100, 101], [100, 101, 200] and [101, 200, 300]

Input: arr[] = [1, 2, 3]
Output: 0
Explanation: No triangles are possible.
"""


def countTriangles(arr):
    # code here
    arr.sort()
    cnt = 0
    n = len(arr)

    for i in range(2, n):
        l, r = 0, i - 1

        while l < r:
            if arr[l] + arr[r] > arr[i]:
                cnt += r - l

                r -= 1
            else:
                l += 1
    return cnt


nums = list(map(int, input().rstrip().split()))
ans = countTriangles(nums)
print("Total Triangles: ", ans)
