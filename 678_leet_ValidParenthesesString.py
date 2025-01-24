"""
678. Valid Parenthesis String
-----------------------------

Note: This problem same as - 2116. Check if a Parentheses String Can Be Valid
                             ------------------------------------------------

problem link - https://leetcode.com/problems/valid-parenthesis-string/

Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".


Example 1:
---------
Input: s = "()"
Output: true

Example 2:
---------
Input: s = "(*)"
Output: true

Example 3:
---------
Input: s = "(*))"
Output: true
"""


def checkValidString(s: str) -> bool:
    # Time Complexity - O(n)
    # Space Complexity - O(1)

    # Two - pass
    openBracket = 0
    star = 0

    for i in range(0, len(s)):
        # check can match
        if s[i] == ")":
            if openBracket:
                openBracket -= 1
            elif star:
                star -= 1
            else:
                return False
        elif s[i] == "(":
            openBracket += 1
        else:
            star += 1
    closeBracket = 0
    star = 0

    for i in range(len(s) - 1, -1, -1):
        # check can match
        if s[i] == "(":
            if closeBracket:
                closeBracket -= 1
            elif star:
                star -= 1
            else:
                return False
        elif s[i] == "(":
            closeBracket += 1
        else:
            star += 1
    return True


s = input()
res = checkValidString(s)
print("Given parenthesis is valid: ", res)

"""
Using leftMin, leftMax two-variable one pass
---------------------------------------------
Example:
  s = "(*))"
  leftMin, leftMax --> Both represents the possibilities of open parenthesis for matching the close parenthesis
  Now look at the string,
     * whenever we encounter "(" increase by one in both
     * whenever we encounter ")" decrease by one in both
     * when "*" arrived Here the trick works 
        * it could be "(" or ")" or empty string
        * so that decrease by one in leftMin(minimum possibilities), increase by one in leftMax(maximum possibilities)
        * Don't need care about if it empty string
     * if leftMax is less than 0 then return false because we can't match further more
     * if leftMin is less than zero then set it as 0 again (Because here we consider this as minimum possibilities)
     * Finally if leftMin == 0 return True else False
     
           (            *              )             )
           lmin = 1    lmin = 0      lmin = -1      lmin = 0
           lmax = 1    lmax = 2      lmax = 1       lmax = 0
       
      
      
    def checkValidString(self, s: str) -> bool:
        # Time Complexity - O(n)
        # Space Complexity - O(1)

        # One - Pass
        leftMin, leftMax = 0, 0

        for i in range(0, len(s)):
            if s[i] == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif s[i] == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1

            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0
        return leftMin == 0

"""