"""
2486. Append Characters to String to Make Subsequence
-----------------------------------------------------

You are given two strings s and t consisting of only lowercase English letters.
Return the minimum number of characters that need to be appended to the end of s so that t becomes a subsequence of s.
A subsequence is a string that can be derived from another string by deleting some or no characters
without changing the order of the remaining characters.

Example 1:
----------
Input: s = "coaching", t = "coding"
Output: 4
Explanation: Append the characters "ding" to the end of s so that s = "coachingding".
Now, t is a subsequence of s ("coachingding").
It can be shown that appending any 3 characters to the end of s will never make t a subsequence.

Example 2:
----------
Input: s = "abcde", t = "a"
Output: 0
Explanation: t is already a subsequence of s ("abcde").

Example 3:
----------
Input: s = "z", t = "abcde"
Output: 5
Explanation: Append the characters "abcde" to the end of s so that s = "zabcde".
Now, t is a subsequence of s ("zabcde").
It can be shown that appending any 4 characters to the end of s will never make t a subsequence.
"""


def appendCharacters(s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    count = 0
    i = 0
    flag = False
    if t == s:  # if the given two strings are same then return 0
        return 0
    elif t in s:
        return 0  # if the string2 characters all available in string 1 then return 0
    else:
        for letter in range(0, len(t)):
            if t[letter] in s:
                flag = False
                for j in range(i, len(s)):
                    if t[letter] == s[j]:  # check the string2 letters in or not in string1
                        flag = True
                        break
                if flag:  # if in
                    count += 1
                    i = j + 1  # increment the index range to reduce time complexity and avoid errors
                else:  # if not in
                    return abs(len(t) - count)
            else:
                break
        return abs(len(t) - count)  # return the minimum number of characters to append 


word1 = input()
word2 = input()
print(appendCharacters(word1, word2))
