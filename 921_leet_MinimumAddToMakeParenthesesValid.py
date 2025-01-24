"""
921. Minimum Add to Make Parentheses Valid
------------------------------------------

problem link - https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

A parentheses string is valid if and only if:

    It is the empty string,
    It can be written as AB (A concatenated with B), where A and B are valid strings, or
    It can be written as (A), where A is a valid string.
    You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
Return the minimum number of moves required to make s valid.



Example 1:
----------
Input: s = "())"
Output: 1

Example 2:
----------
Input: s = "((("
Output: 3
"""


def minAddToMakeValid(s):
    # Time Complexity - O(n)
    # Space Complexity - O(1)

    left = 0  # open parenthesis

    res = 0
    for i in range(0, len(s)):
        if s[i] == "(":
            left += 1
        else:
            # if ")" can't match with "(" then update the res
            if left < 1:
                res += 1
            # if ")" can match with "(" ,then decrease the left by one
            else:
                left -= 1
    # add left to result if any "(" still there
    return res + left


s = input()
ans = minAddToMakeValid(s)
print("Total insertion for add: ", ans)