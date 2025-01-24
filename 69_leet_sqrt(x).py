"""
69. Sqrt(x)
-----------

Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Example 1:
----------
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:
----------
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
"""


# algorithm works reduce the given number with odd numbers from 1,3,5,7..... until the number <= 0
# increment the count value in each reduce operation
def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    if x == 1:
        return 1
    count = 0
    square_root = 0
    i = 1
    while x >= 0:  # 4
        x -= i  # 4-1 = 3, 3-3 = 0
        count += 1  # count = 1, count = 2
        if x == 0:
            square_root = count
            break
        elif x < 0:
            count -= 1
            square_root = count
            break
        i += 2
    return square_root


number = int(input())  # 4
print(mySqrt(number))
