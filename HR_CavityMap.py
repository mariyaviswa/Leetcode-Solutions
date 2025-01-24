"""
You are given a square map as a matrix of integer strings. Each cell of the map has a value denoting its depth.
We will call a cell of the map a cavity if and only if this cell is not on the border of the map and each cell adjacent
to it has strictly smaller depth. Two cells are adjacent if they have a common side, or edge.
Find all the cavities on the map and replace their depths with the uppercase character X.
Example
-------
grid = ['989', '191', '111']

The grid is rearranged for clarity:
----------------------------------
    989
    191
    111
Return:
-------
    989
    1X1
    111
The center cell was deeper than those on its edges: [8,1,1,1].
The deep cells in the top two corners do not share an edge with the center cell, and none of the border cells is eligible.

Sample Input
------------
    STDIN   Function
    -----   --------
    4       grid[] size n = 4
    1112    grid = ['1112', '1912', '1892', '1234']
    1912
    1892
    1234
    Sample Output
    -------------

    1112
    1X12
    18X2
    1234
Explanation
-----------
The two cells with the depth of 9 are not on the border and are surrounded on all sides by shallower cells.
Their values are replaced by X.
"""


def cavityMap(grid):
    # Write your code here
    if len(grid) == 1:
        return grid
    length = len(grid[0])
    final = []
    final.append(grid[0])
    for i in range(1, length - 1):
        result = ""
        result += grid[i][0]
        for j in range(1, length - 1):
            if (int(grid[i][j]) > int(grid[i - 1][j]) and int(grid[i][j]) > int(grid[i + 1][j])) and (
                    int(grid[i][j]) > int(grid[i][j - 1]) and int(grid[i][j]) > int(grid[i][j + 1])):
                result += 'X'
            else:
                result += grid[i][j]
        result += grid[i][length - 1]
        final.append(result)
    final.append(grid[length - 1])
    return final


Grid = list(map(str, input().rstrip().split()))
print(cavityMap(Grid))
