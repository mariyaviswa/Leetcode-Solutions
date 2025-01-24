"""
2559. Count Vowel Strings in Ranges
-----------------------------------

problem link - https://leetcode.com/problems/count-vowel-strings-in-ranges/

You are given a 0-indexed array of strings words and a 2D array of integers queries.

Each query queries[i] = [li, ri] asks us to find the number of strings present in the range li to ri (both inclusive)
of words that start and end with a vowel.

Return an array answer of size queries.length, where ans[i] is the answer to the ith query.

Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.



Example 1:
---------
Input: words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]
Output: [2,3,0]
Explanation: The strings starting and ending with a vowel are "aba", "ece", "aa" and "e".
The answer to the query [0,2] is 2 (strings "aba" and "ece").
to query [1,4] is 3 (strings "ece", "aa", "e").
to query [1,1] is 0.
We return [2,3,0].

Example 2:
---------
Input: words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]
Output: [3,2,1]
Explanation: Every string satisfies the conditions, so we return [3,2,1].

"""


def vowelStrings(words, queries):
    # Time Complexity - O(n)
    # Space Complexity - O(n)
    vowels = set("aeiou")
    n = len(words)
    indices = [0] * (n + 1)

    for i in range(0, n):

        if words[i][0] in vowels and words[i][-1] in vowels:
            indices[i + 1] += indices[i] + 1  # prefix sum
        else:
            indices[i + 1] = indices[i]

    res = [0] * len(queries)
    for i, q in enumerate(queries):
        res[i] = indices[q[1] + 1] - indices[q[0]]
    return res


strs = list(map(str, input().rstrip().split()))
m = int(input())
query = []
for i in range(m):
    inp = list(map(int, input().rstrip().split()))
    query.append(inp)
ans = vowelStrings(strs, query)
