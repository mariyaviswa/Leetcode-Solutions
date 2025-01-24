"""
171. Excel Sheet Column Number
------------------------------
problem link - https://leetcode.com/problems/excel-sheet-column-number/

Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

For example:
-----------
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...


Example 1:
---------
Input: columnTitle = "A"
Output: 1

Example 2:
----------
Input: columnTitle = "AB"
Output: 28

Example 3:
----------
Input: columnTitle = "ZY"
Output: 701
"""


def titleToNumber(columnTitle):
    # Time Complexity - O(n)
    # Space Complexity - O(1)
    colNumber = 0
    exp = 0
    for ch in columnTitle[::-1]:
        num = (ord(ch) - ord("A")) + 1
        colNumber += num * (26 ** exp)
        exp += 1
    return colNumber


title = input()
res = titleToNumber(title)
print("Column Number: ", res)
