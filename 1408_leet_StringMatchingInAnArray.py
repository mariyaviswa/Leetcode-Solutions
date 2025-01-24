"""
1408. String Matching in an Array
---------------------------------

problem link - https://leetcode.com/problems/string-matching-in-an-array/

Given an array of string words, return all strings in words that is a substring of another word.
You can return the answer in any order.

A substring is a contiguous sequence of characters within a string



Example 1:
---------
Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.

Example 2:
---------
Input: words = ["leetcode","et","code"]
Output: ["et","code"]
Explanation: "et", "code" are substring of "leetcode".

Example 3:
---------
Input: words = ["blue","green","bu"]
Output: []
Explanation: No string of words is substring of another string.
"""


def stringMatching(words):
    # Time Complexity - O(n^2)
    # Space Complexity - O(n)
    res = []
    for i in range(0, len(words)):
        for j in range(0, len(words)):
            if i == j:
                continue

            if words[i] in words[j]:
                res.append(words[i])
                break
    return res


word = list(map(str, input().rstrip().split()))
ans = stringMatching(word)
print("The substrings of other words: ", ans)
