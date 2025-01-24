"""
6. Zigzag Conversion
--------------------

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

        P   A   H   N
        A P L S I I G
        Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

Example 1:
---------
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
----------
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
        0-P     6 - I       12- N
        1-A   5-L 7-S  11-I 13-G
        2-Y 4-A   8-H 10-R
        3-P       9-I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
"""


def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    centre = (numRows - 1) * 2  # for identify each column
    k = numRows - 2
    dictionary = {}  # to store each rows string value
    for i in range(numRows):
        dictionary[i] = ""  # assign each row an empty string
    i = 0
    while len(s) > 0:
        # see the example 2 for better clarification
        if 0 <= i < numRows and i < len(s):  # append letters in its row
            dictionary[i] += s[i]
            i += 1
        elif numRows <= i < centre and i < len(s):  # when i == numRow(i.e, this for  cross letters
            dictionary[k] += s[i]
            k -= 1
            i += 1
        else:
            s = s[i:]
            k = numRows - 2
            i = 0
    result = ""
    for i in dictionary.values():
        result += i
    return result


string = input()
numrows = int(input())
print(convert(string, numrows))