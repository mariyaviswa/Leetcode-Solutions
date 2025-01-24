"""
1400. Construct K Palindrome Strings
------------------------------------

problem link - https://leetcode.com/problems/construct-k-palindrome-strings/

Given a string s and an integer k, return true if you can use all the characters in s to
construct k palindrome strings or false otherwise.



Example 1:
----------
Input: s = "annabelle", k = 2
Output: true
Explanation: You can construct two palindromes using all characters in s.
Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "b"

Example 2:
----------
Input: s = "leetcode", k = 3
Output: false
Explanation: It is impossible to construct 3 palindromes using all the characters of s.

Example 3:
----------
Input: s = "true", k = 4
Output: true
Explanation: The only possible solution is to put each character in a separate string.

"""
from collections import Counter


def canConstruct(s, k):
    # Time Complexity - O(n)
    # Space Complexity - O(n)
    if len(s) < k:
        return False

    counts = Counter(s)

    odd = 0
    for v in counts.values():
        if v % 2 != 0:
            odd += 1

    return odd <= k


s = input()
n = int(input())
res = canConstruct(s, n)
print(f"Can Construct {n} Palindromes: ", res)