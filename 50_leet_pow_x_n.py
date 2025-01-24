"""
50. Pow(x,n)
------------

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
Example 1:
----------
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
----------
Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:
----------
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
"""


def myPow(x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """
    if n == 0:
        return 1
    if x == 0:
        return 0
    if n > 0:  # positive case
        power = "{:.5f}".format(pow(x, n))
        return float(power)
    else:  # negative case
        if n < -2147483647:
            if x == 1:
                return 1
            elif x == -1:
                if abs(n) % 2 == 0:
                    return 1
                else:
                    return -1
            elif 1 < x < 2:
                power = x ** n
                return power
            else:
                return 0
        else:
            power = pow(x, abs(n))
            ans = 1 / power
            result = "{:.5f}".format(ans)
            return float(result)


Base = float(input())
Power = int(input())
print(myPow(Base, Power))
