"""
MATRIX LAYER ROTATION (HARD)
----------------------------

You are given a 2D matrix of dimension mxn and a positive integer r. You have to rotate the matrix r times and print the resultant matrix.
Rotation should be in anti-clockwise direction.

It is guaranteed that the minimum of m and n will be even.

As an example rotate the Start matrix by 2:

    Start         First           Second
     1 2 3 4       2  3  4  5      3  4  5  6
    12 1 2 5  ->   1  2  3  6 ->   2  3  4  7
    11 4 3 6      12  1  4  7      1  2  1  8
    10 9 8 7      11 10  9  8     12 11 10  9

Sample Input
------------
Sample Input #01
----------------

STDIN        Function
-----        --------
4 4 2        rows m = 4, columns n = 4, rotation factor r = 2
1 2 3 4      matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
5 6 7 8
9 10 11 12
13 14 15 16

Sample Output #01
-----------------
3 4 8 12
2 11 10 16
1 7 6 15
5 9 13 14

Explanation #01

The matrix is rotated through two rotations.

     1  2  3  4      2  3  4  8      3  4  8 12
     5  6  7  8      1  7 11 12      2 11 10 16
     9 10 11 12  ->  5  6 10 16  ->  1  7  6 15
    13 14 15 16      9 13 14 15      5  9 13 14

Sample Input #02
----------------
5 4 7
1 2 3 4
7 8 9 10
13 14 15 16
19 20 21 22
25 26 27 28
Sample Output #02
-----------------
28 27 26 25
22 9 15 19
16 8 21 13
10 14 20 7
4 3 2 1

Explanation 02

The various states through 7 rotations:

    1  2  3  4      2  3  4 10    3  4 10 16    4 10 16 22
    7  8  9 10      1  9 15 16    2 15 21 22    3 21 20 28
    13 14 15 16 ->  7  8 21 22 -> 1  9 20 28 -> 2 15 14 27 ->
    19 20 21 22    13 14 20 28    7  8 14 27    1  9  8 26
    25 26 27 28    19 25 26 27    13 19 25 26   7 13 19 25

    10 16 22 28    16 22 28 27    22 28 27 26    28 27 26 25
     4 20 14 27    10 14  8 26    16  8  9 25    22  9 15 19
     3 21  8 26 ->  4 20  9 25 -> 10 14 15 19 -> 16  8 21 13
     2 15  9 25     3 21 15 19     4 20 21 13    10 14 20  7
     1  7 13 19     2  1  7 13     3  2  1  7     4  3  2  1

Sample Input #03
----------------
2 2 3
1 1
1 1
Sample Output #03
-----------------
1 1
1 1

Explanation #03

All the elements are the same, so any rotation will repeat the same matrix.
"""
# get inputs
get_inp = list(map(int, input().rstrip().split()))
m = get_inp[0]
n = get_inp[1]
rotate = get_inp[2]
matrix = []
for i in range(m):
    inp = list(map(int, input().rstrip().split()))
    matrix.append(inp)

# calculate the total layers in the matrix
length = min(m, n) // 2

#  for find each layer's starting and ending point
l, r = 0, n - 1
row = m - 1
# run this loop upto length + 1
for i in range(1, length + 1):
    count = (r - l) * 2 + (row - l) * 2  # calculate the full rotation for each layer
    rot = rotate % count  # get the accurate rotation for each layer (for reduce time complexity)
    for j in range(0, rot):  # run this loop no of rot
        temp = matrix[l][l]  # in each layer store the starting element in temp variable
        # left to right
        for s1 in range(l, r):
            matrix[l][s1] = matrix[l][s1 + 1]
        # top to bottom
        for s2 in range(l, row):
            matrix[s2][r] = matrix[s2 + 1][r]
        # right to left
        for s3 in range(r, l, -1):
            matrix[row][s3] = matrix[row][s3 - 1]
        # bottom to top
        for s4 in range(row, l + 1, -1):
            matrix[s4][l] = matrix[s4 - 1][l]
        matrix[l + 1][l] = temp
    # increment the starting point, and decrement the ending point for each layer
    l += 1
    r -= 1
    row -= 1

# finally print each layer of rotated matrix
for val in matrix:
    print(*val, sep=' ')
