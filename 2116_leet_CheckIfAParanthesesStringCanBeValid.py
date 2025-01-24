"""
2116. Check if a Parentheses String Can Be Valid
------------------------------------------------
Problem link - https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/

A parentheses string is a non-empty string consisting only of '(' and ')'.
It is valid if any of the following conditions is true:

    It is ().
    It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
    It can be written as (A), where A is a valid parentheses string.
    You are given a parentheses string s and a string locked, both of length n.
    locked is a binary string consisting only of '0's and '1's. For each index i of locked,

    If locked[i] is '1', you cannot change s[i].
    But if locked[i] is '0', you can change s[i] to either '(' or ')'.
    Return true if you can make s a valid parentheses string. Otherwise, return false.



Example 1:
----------
Input: s = "))()))", locked = "010100"
Output: true
Explanation: locked[1] == '1' and locked[3] == '1', so we cannot change s[1] or s[3].
We change s[0] and s[4] to '(' while leaving s[2] and s[5] unchanged to make s valid.

Example 2:
----------
Input: s = "()()", locked = "0000"
Output: true
Explanation: We do not need to make any changes because s is already valid.

Example 3:
----------
Input: s = ")", locked = "0"
Output: false
Explanation: locked permits us to change s[0].
Changing s[0] to either '(' or ')' will not make s valid.
"""


def canBeValid(s, locked):
    # Time Complexity - O(n)
    # Space Complexity - O(1)

    # Two - pass
    n = len(s)
    # Odd length of string(parentheses) can't valid
    if n & 1: return False

    unLocked, openLocked = 0, 0

    for p, c in zip(s, locked):

        #  left to right check the locked close parentheses
        #  Check also it can be valid or not
        if p == ")" and c == "1":
            if openLocked:
                openLocked -= 1
            elif unLocked:
                unLocked -= 1
            else:
                return False
        elif p == "(" and c == "1":
            openLocked += 1
        else:
            unLocked += 1

    unLocked, closedLocked = 0, 0

    for p, c in zip(s[::-1], locked[::-1]):

        #  right to left check the locked open parentheses
        #  Check also it can be valid or not
        if p == "(" and c == "1":
            if closedLocked:
                closedLocked -= 1
            elif unLocked:
                unLocked -= 1
            else:
                return False
        elif p == ")" and c == "1":
            closedLocked += 1
        else:
            unLocked += 1
    return True


par = input()
status = input()
res = canBeValid(par, status)
print(f"{par} is valid: ", res)

"""
Using stack
-----------

    def canBeValid(self, s: str, locked: str) -> bool:
        # Time Complexity - O(n)
        # Space Complexity - O(n)

        n = len(s)
        if n & 1: return False

        Locked = []
        unLocked = []
        i = 0
        for b, c in zip(s, locked):
            if b == ")" and c == "1":
                if Locked:
                    Locked.pop()
                elif unLocked:
                    unLocked.pop()
                else:
                    return False
            elif b == "(" and c == "1":
                Locked.append(i)
            else:
                unLocked.append(i)
            i += 1

        while Locked:
            if unLocked and Locked[-1] < unLocked[-1]:
                Locked.pop()
                unLocked.pop()
            else:
                return False
        return True
"""
