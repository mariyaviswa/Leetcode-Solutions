"""
766. Toeplitz Matrix
--------------------

Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

Example 1:
---------
Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: true
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.

                        1   2   3   4

                        5   1   2   3

                        9   5   1   2
Example 2:
----------
Input: matrix = [[1,2],[2,2]]
Output: false
Explanation:
The diagonal "[1, 2]" has different elements.
"""


def isToeplitzMatrix(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: bool
    """
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            #  Check whether each value is equal to the value of it's top-left neighbor.
            if matrix[i][j] != matrix[i - 1][j - 1]:
                return False
    return True


row = int(input())
column = int(input())
Matrix = []
for i in range(row):
    inp = list(map(int, input().rstrip().split()))
    Matrix.append(inp)
print(isToeplitzMatrix(Matrix))
