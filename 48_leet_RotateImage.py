"""
48. Rotate Image
----------------

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.

         1 2 3     7 8 9    7 4 1    7 4 1
         4 5 6 ->  4 5 6 -> 8 5 6 -> 8 5 2
         7 8 9     1 2 3    9 2 3    9 6 3

Example 1:
----------
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
----------
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
"""


def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    # Reverse the matrix
    for i in range(0, len(matrix[0]) // 2):
        matrix[i], matrix[len(matrix[0]) + (-1 - i)] = matrix[len(matrix) + (-1 - i)], matrix[i]

    for i in range(0, len(matrix[0]) - 1):  # After take each row
        for j in range(i + 1, len(matrix[0])):  # from row + 1,  change the value
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix


n = int(input())
Matrix = []
for i in range(n):
    inp = list(map(int, input().rstrip().split()))
    Matrix.append(inp)
print(rotate(Matrix))
