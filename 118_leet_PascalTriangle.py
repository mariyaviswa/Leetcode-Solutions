"""
118. Pascal's Triangle
----------------------

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
Example:
-------
n = 5 , the triangle shown below

                    1
                  1   1
                1   2   1
              1   3    3   1
            1   4   6    4   1


Example 1:
---------
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
---------
Input: numRows = 1
Output: [[1]]
"""


def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    if numRows == 1:
        return [[1]]
    elif numRows == 2:
        return [[1], [1, 1]]
    else:
        vals = [[1], [1, 1]]
        j = 2
        while j < numRows:
            triangle = []
            triangle.append(vals[-1][0])  # append the last index's first value from vals list
            for i in range(1, len(vals[-1])):
                triangle.append(vals[-1][i] + vals[-1][i - 1])  # add current val + prev val ( perform in the last index in vals)
            triangle.append(vals[-1][-1])  # append the last index's last value from vals list
            j += 1
            vals.append(triangle)
        return vals


Numrows = int(input())
print(generate(Numrows))
