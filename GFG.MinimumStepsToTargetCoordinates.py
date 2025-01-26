"""
Minimum Steps to Target Coordinate
----------------------------------

You are positioned at the origin (0, O) on a 2D Cartesian plane, and your objective is to
reach a target point (x, y). In each move, you can choose to travel either 2 units or 4 units in
one of the four cardinal directions: Up, Down, Left, or Right.
Your task is to determine the minimum number of moves needed to reach the target
coordinate (x, y). If it is impossible to reach the target using the specified movements,
return -1.
"""


def minOperations(x: int, y: int) -> int:
    # code here
    x = abs(x)
    y = abs(y)
    if x % 2 == 0 and y % 2 == 0:
        four_x = x // 4
        x -= (four_x * 4)
        two_x = x // 2

        four_y = y // 4
        y -= (four_y * 4)
        two_y = y // 2

        return (four_x + two_x) + (four_y + two_y)
    else:
        return -1


x = int(input())
y = int(input())
print(minOperations(x, y))
