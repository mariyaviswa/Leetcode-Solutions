"""
916. Word Subsets
-----------------

problem link - https://leetcode.com/problems/word-subsets/

You are given two string arrays words1 and words2.

A string b is a subset of string a if every letter in b occurs in an including multiplicity.

For example, "wrr" is a subset of "warrior" but is not a subset of "world".
A string a from words1 is universal if for every string b in words2, b is a subset of a.

Return an array of all the universal strings in words1. You may return the answer in any order.



Example 1:
---------
Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
Output: ["facebook","google","leetcode"]

Example 2:
----------
Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]
Output: ["apple","google","leetcode"]
"""


from collections import Counter


def wordSubsets(words1, words2):
    # Time Complexity - O(n + m)
    # Space Complexity - O(max(n,m))
    allWords = {}

    for w in words2:
        temp = Counter(w)
        for k, v in temp.items():
            if k not in allWords:
                allWords[k] = v
            else:
                allWords[k] = max(v, allWords[k])

    res = []
    for w1 in words1:
        tmp = Counter(w1)

        flag = True
        for k, v in allWords.items():
            if k not in tmp or v > tmp[k]:
                flag = False
                break
        if flag:
            res.append(w1)
    return res


word1 = list(map(str, input().split()))
word2 = list(map(str, input().split()))

ans = wordSubsets(word1, word2)

print()
