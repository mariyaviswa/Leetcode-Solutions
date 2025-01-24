"""
256. Paint House
----------------

There are a row of n houses, each house can be painted with one of the three colors: red, blue or green.
The cost of painting each house with a certain color is different.
You have to paint all the houses such that no two adjacent houses have the same color, and you need to cost the least.
Return the minimum cost.

The cost of painting each house with a certain color is represented by an n x 3 cost matrix.
For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green,
and so on... Find the minimum cost to paint all houses.

Example 1:
----------

Understanding:
-------------
    the array is like [red, blue, green] --> the cost of each color
    if [14, 2, 11] then
       the cost of painting with red color for the house 1 is 14
       the cost of painting with blue color for the house 1 is 2
       the cost of painting with green color for the house 1 is 11


Input: [[14,2,11],[11,14,5],[14,3,10]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue. Minimum cost: 2 + 5 + 3 = 10.

Let's take 3 x 3
----------------
                    14                    2                      11

                    11 + min(2, 11)    14 + min(14, 11)     5 + min(14, 2)
                    13                    25                      7

                    14 + min(25, 7)    3 + min(13, 7)       10 + min(13, 25)
                    21                    10                      23

 * Here Look at the above , For the first row we can't do anything
(Because in the starting we can't pick any value to make min_cost it won't make any sense)

* So start from the second row use dp = [0, 0, 0], or we can do in-place
for the first house first index(i.e, 0th index) the value 11, and we add the minimum of the previous row's 1st and 2nd value
* Because we can't use the same color for the adjacent row
* Like wise we will do the all index and all other rows
* At last from the last row, we can find the minimum cost to paint
* so take the minimum value from the last row
* So, the final answer is min([21, 10, 23]) = 10.

Example 2:
---------
Input: [[1,2,3],[1,4,6]]
Output: 3
"""


def minCost(costs):
    # costs[i][j], i - house, j - color

    for i in range(1, len(costs)):
        costs[i][0] += min(costs[i - 1][1], costs[i - 1][2])
        costs[i][1] += min(costs[i - 1][0], costs[i - 1][2])
        costs[i][2] += min(costs[i - 1][0], costs[i - 1][1])
    return min(costs[-1])


cost = []
n = int(input())
for i in range(0, n):
    arr = list(map(int, input().rstrip().split()))
    cost.append(arr)
res = minCost(cost)
print("The minimum cost: ", res)
