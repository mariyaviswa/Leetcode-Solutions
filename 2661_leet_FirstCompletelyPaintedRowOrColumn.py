"""
2661. First Completely Painted Row or Column
--------------------------------------------

problem link - https://leetcode.com/problems/first-completely-painted-row-or-column/

You are given a 0-indexed integer array arr, and an m x n integer matrix mat.
arr and mat both contain all the integers in the range [1, m * n].

Go through each index i in arr starting from index 0 and paint the cell in mat containing the integer arr[i].

Return the smallest index i at which either a row or a column will be completely painted in mat.



Example 1:
----------
image explanation for example 1
Input: arr = [1,3,4,2], mat = [[1,4],[2,3]]
Output: 2
Explanation: The moves are shown in order, and both the first row and second column of the matrix become fully painted at arr[2].

Example 2:
---------
image explanation for example 2
Input: arr = [2,8,7,4,1,3,5,6,9], mat = [[3,2,5],[1,4,6],[8,7,9]]
Output: 3
Explanation: The second column becomes fully painted at arr[3].
"""


def firstCompleteIndex(arr: list[int], mat: list[list[int]]) -> int:
    # Time Complexity - O(mn)
    # Space Complexity - O(mn)
    m = len(mat)
    n = len(mat[0])

    # For track the painted cells
    row = [0] * m
    col = [0] * n

    nums = {}  # store the positions of each value that present in the arr
    for i in range(0, len(mat)):
        for j in range(0, len(mat[0])):
            nums[mat[i][j]] = (i, j)

    for i in range(0, len(arr)):
        idx = nums[arr[i]]
        # increase the row count
        row[idx[0]] += 1
        # increase the col count
        col[idx[1]] += 1

        # if any row or col fully painted
        if row[idx[0]] == n or col[idx[1]] == m:
            return i


nums = list(map(int, input().split()))
m = int(input())  # row
matrix = []
for i in range(m):
    inp = list(map(int, input().split()))
    matrix.append(inp)

res = firstCompleteIndex(nums, matrix)
print("First painted row or column at index: ", res)
