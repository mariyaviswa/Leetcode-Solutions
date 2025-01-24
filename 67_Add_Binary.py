"""
67. Add Binary
--------------

Given two binary strings a and b, return their sum as a binary string.
Example 1:
----------
Input: a = "11", b = "1"
Output: "100"

Example 2:
----------
Input: a = "1010", b = "1011"
Output: "10101"
"""


def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    sum1 = 0
    sum2 = 0
    i = 0
    while i < len(a):
        # perform the normal binary operation to find the decimal form from right to left with multiply the first int in the binary with 2 power 0
        # then second number with 2 pow 1 and so 2 pow 2,...n
        sum1 += int(a[-i - 1]) * (2 ** i)
        i += 1

    j = 0
    while j < len(b):
        # perform the normal binary operation to find the decimal form from right to left with multiply the first int in the binary with 2 power 0
        # then second number with 2 pow 1 and so 2 pow 2,...n
        sum2 += int(b[-j - 1]) * (2 ** j)
        j += 1
    binary = bin(sum1 + sum2)
    binary = str(binary)
    return binary[2:]


binary1 = str(input())
binary2 = str(input())
print(addBinary(binary1, binary2))
