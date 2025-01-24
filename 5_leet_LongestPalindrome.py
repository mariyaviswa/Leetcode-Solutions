"""
5. Longest Palindromic Substring
--------------------------------

Given a string s, return the longest palindromic substring in s.

Example 1:
---------
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
----------
Input: s = "cbbd"
Output: "bb"
"""


def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    if len(s) == 1 or len(s) == 0:
        return s
    elif len(s) == 2:
        if s == s[-1:-len(s) - 1:-1]:
            return s
        else:
            return s[0]
    else:
        if s == s[-1:-len(s) - 1:-1]:
            return s
        else:
            palindromes = []
            for i in range(0, len(s)):
                sub_string = ""
                sub_string += s[i]
                for j in range(i + 1, len(s)):
                    sub_string += s[j]
                    if sub_string == sub_string[-1:-len(sub_string) - 1:-1]:
                        palindromes.append(sub_string)
            if palindromes:
                for i in range(1, len(palindromes)):
                    if len(palindromes[0]) < len(palindromes[i]):
                        palindromes[0] = palindromes[i]
                return palindromes[0]
            else:
                return s[0]


String = input()
print(longestPalindrome(String))
