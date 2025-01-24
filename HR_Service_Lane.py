"""
A driver is driving on the freeway. The check engine light of his vehicle is on, and the driver wants to get service immediately.
Luckily, a service lane runs parallel to the highway. It varies in width along its length.

You will be given an array of widths at points along the road (indices), then a list of the indices of entry and exit points.
Considering each entry and exit point pair, calculate the maximum size vehicle that can travel that segment of the service lane safely.

Example
-------
n = 4
width = [2,3,2,1]
cases = [[1,2],[2,4]]

If the entry index,i = 1  and the exit,j = 2 , there are two segment widths of 2  and 3 respectively.
The widest vehicle that can fit through both is 2. If i = 2 and j = 4, the widths are [3,2,1] which limits vehicle width to 1.

Sample Input
------------

STDIN               Function
-----               --------
8 5                 n = 8, t = 5
2 3 1 2 3 2 3 3     width = [2, 3, 1, 2, 3, 2, 3, 3]
0 3                 cases = [[0, 3], [4, 6], [6, 7], [3, 5], [0, 7]]
4 6
6 7
3 5
0 7

Sample Output
---------------
1
2
3
2
1

Explanation
-----------
Below is the representation of the lane:

   |HIGHWAY|Lane|    ->    Width

0: |       |--|            2
1: |       |---|           3
2: |       |-|             1
3: |       |--|            2
4: |       |---|           3
5: |       |--|            2
6: |       |---|           3
7: |       |---|           3

1.(0,3): From index 0 through 3 we have widths 2, 3, 1 and 2. Nothing wider than 1 can pass all segments.
2.(4,6): From index 4 through 6 we have width 3, 2 and 3. Nothing wider than 2 can pass all segments.
3. (6, 7):3,3 -> 3.
4.(3,5): 2,3,2 -> 2
5.(0, 7): 2, 3, 1, 2, 3, 2, 3,3 -> 1.

"""


def serviceLane(n, cases, width):
    # Write your code here
    result = []
    for i in range(0, len(cases)):
        minimum = min(width[cases[i][0]:cases[i][1] + 1])
        result.append(minimum)
    return result


first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
t = int(first_multiple_input[1])
width = list(map(int, input().rstrip().split()))
cases = []
for _ in range(t):
    cases.append(list(map(int, input().rstrip().split())))

result = serviceLane(n, cases, width)
print(result)
