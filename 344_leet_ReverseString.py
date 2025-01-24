"""
344. Reverse String
-------------------

Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.
Example 1:
----------
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
----------
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""


def reverseString(s):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    length = len(s) // 2
    for i in range(0, length):
        s[i], s[len(s) - (i + 1)] = s[len(s) - (i + 1)], s[i]
    # Time complexity low
    # s.reverse() # Time complexity and  optimized
    return s


String = list(map(str, input().rstrip().split()))
print(reverseString(String))
