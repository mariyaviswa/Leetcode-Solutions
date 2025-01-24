"""
73. Set Matrix Zeroes
---------------------

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.
Example 1:
---------
    1 1 1      1 0 1
    1 0 1  ->  0 0 0
    1 1 1      1 0 1
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
"""


def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    zeros = {}
    val = []
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if matrix[i][j] == 0:  # find the value 0 in each row
                val.append(j)
                zeros[i] = val
    # for s in zeros[0]:
    #     print(s)
    for row_val in zeros.keys():
        for col_val in zeros[row_val]:
            k = 0
            while k < len(matrix[0]):  # change the row val as 0
                matrix[row_val][k] = 0
                k += 1
            j = 0
            while j < len(matrix):  # change the column val as 0
                matrix[j][col_val] = 0
                j += 1
    return matrix  # return converted matrix


Matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
print(setZeroes(Matrix))
