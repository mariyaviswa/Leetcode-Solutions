"""
7. Reverse Integer
------------------

Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""


def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    x = str(x)  # convert the int to str to perform operations
    reverse_integer = ""
    # if the integer have symbol the add to reverse_integer and remove from given integer
    if x[0] == "-" or x[0] == "+":
        reverse_integer += x[0]
        x = x[1:]
    reverse_integer += x[-1:-len(x) - 1:-1]  # perform indexing operation to convert it reverse
    if -2 ** 31 <= int(reverse_integer) <= (2 ** 31) - 1:
        return int(reverse_integer)
    else:
        return 0


number = int(input())
print(reverse(number))
