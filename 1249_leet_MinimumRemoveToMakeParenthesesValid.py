"""
1249. Minimum Remove to Make Valid Parentheses
----------------------------------------------

problem link - https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions )
so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.


Example 1:
---------
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example 2:
----------
Input: s = "a)b(c)d"
Output: "ab(c)d"

Example 3:
----------
Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
"""


def minRemoveToMakeValid(s: str) -> str:
    # Time Complexity - O(n)
    # Space Complexity - O(n)

    stack = []
    s = list(s)  # converting str to list can access the particular index
    for i in range(0, len(s)):
        if s[i] == "(":
            stack.append(i)
        elif s[i] == ")":
            # if any match found
            if stack:
                stack.pop()
            else:
                s[i] = ''  # if not found set as empty string
    # check the remaining open parenthesis
    while stack:
        s[stack[-1]] = ''  # set as empty string
        stack.pop()
    # return the string after removing unmatched parenthesis
    return "".join(s)


s = input()
res = minRemoveToMakeValid(s)
print("The final string: ", res)