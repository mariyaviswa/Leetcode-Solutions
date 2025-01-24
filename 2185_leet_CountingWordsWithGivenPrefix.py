"""
2185. Counting Words With a Given Prefix
----------------------------------------

problem link -https://leetcode.com/problems/counting-words-with-a-given-prefix/

You are given an array of strings words and a string pref.

Return the number of strings in words that contain pref as a prefix.

A prefix of a string s is any leading contiguous substring of s.



Example 1:
---------
Input: words = ["pay","attention","practice","attend"], pref = "at"
Output: 2
Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend".

Example 2:
---------
Input: words = ["leetcode","win","loops","success"], pref = "code"
Output: 0
Explanation: There are no strings that contain "code" as a prefix.
"""


def prefixCount(words, pref):
    # Time Complexity - O(n*m)
    # n - length of total words, m - the prefix length for comparison
    # Space Complexity - o(m)
    cnt = 0
    for w in words:
        n, m = len(w), len(pref)
        if n >= m and w[:m] == pref:
            cnt += 1

    return cnt


strs = list(map(str, input().rstrip().split()))
prefix = input()
res = prefixCount(strs, prefix)
print("Total prefix words: ", res)

"""
    # Time Complexity - O(n)
    # Space Complexity - o(1)
    
    def prefixCount(self, words: List[str], pref: str) -> int:
        # Time Complexity - O(n)
        # Space Complexity - o(1)
        cnt = 0
        m = len(pref)
        for w in words:
            if len(w) < m:
                continue
            flag = 1
            for i in range(m):
                if w[i] != pref[i]:
                    flag = 0
                    break
            cnt += flag
        return cnt

        return cnt
"""
