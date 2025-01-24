"""
242. Valid Anagram
------------------

Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
---------
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
---------
Input: s = "rat", t = "car"
Output: false
"""


def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    for t1 in t:
        if t1 in s:
            s = s.replace(t1, '', 1)
            t = t.replace(t1, '', 1)
        else:
            return False
    if not t and not s:
        return True


String1 = input()
String2 = input()
print(isAnagram(String1, String2))
