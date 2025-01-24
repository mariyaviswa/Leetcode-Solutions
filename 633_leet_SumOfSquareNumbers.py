import math

"""
633. Sum of Square Numbers
--------------------------

Given a non-negative integer c, decide whether there're two integers a and b such that a^2 + b^2 = c.( a==b, a,b>=0)

Example 1:
----------
Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5

Example 2:
----------
Input: c = 3
Output: false
"""


def judgeSquareSum(c):
    """
    :type c: int
    :rtype: bool
    """
    root = round(math.sqrt(c))  # find the square root value of the given number to check from 0 to this limit
    # Two-pointer
    start = 0
    end = int(root)
    """
    c = 5
    start = 0
    end = 2
    1st ---> 0^2 + 2^2 = 4  , Here 4 is less than 5 so increment start
    2nd ---> 1^2 + 2^2 = 5 , Now got it
    """
    while start <= end:
        if (start * start) + (end * end) == c:
            return True
        elif (start * start) + (end * end) > c:
            end -= 1
        else:
            start += 1
    return False  # if no possible numbers there then return false


number = int(input())
print(judgeSquareSum(number))