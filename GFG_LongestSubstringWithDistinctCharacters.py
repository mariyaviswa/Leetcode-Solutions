"""
Longest substring with distinct characters
------------------------------------------

problem link - https://www.geeksforgeeks.org/problems/longest-distinct-characters-in-string5848/1

Given a string s, find the length of the longest substring with all distinct characters.

Examples:
---------
Input: s = "geeksforgeeks"
Output: 7
Explanation: "eksforg" is the longest substring with all distinct characters.

Input: s = "aaa"
Output: 1
Explanation: "a" is the longest substring with all distinct characters.

Input: s = "abcdefabcbb"
Output: 6
Explanation: The longest substring with all distinct characters is "abcdef", which has a length of 6.
"""


def longestUniqueSubstr(s):
    # code here
    # Time Complexity - O(n)
    # Space Complexity - O(1)
    chars = set()

    l = 0
    r = 0
    res = 0
    while r < len(s):
        if s[r] in chars:

            res = max(res, r - l)  # Update the length of substring
            while chars and s[r] in chars:  # If any char found then remove from leftmost value of string in set
                chars.remove(s[l])
                l += 1

        chars.add(s[r])
        r += 1

    res = max(res, r - l)
    return res


"""
without Using set()
-------------------
def longestUniqueSubstr(self, s):
        # code here
        # Time Complexity - O(n)
        # Space Complexity - O(1)
        chars = []
        
        l = 0
        r = 0
        res = 0
        while r < len(s):
            if s[r] not in s[l:r]:
                r += 1
            else:
                res = max(res, r - l)
                l += 1
        res = max(res, r - l)
        return res
"""

s = input()
ans = longestUniqueSubstr(s)
print("The maximum substring length without repeating characters: ", ans)