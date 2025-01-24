"""
409. Longest Palindrome
-----------------------

Given a string s which consists of lowercase or uppercase letters, return the length of the longest
palindrome
 that can be built with those letters.

Letters are case-sensitive, for example, "Aa" is not considered a palindrome.

Example 1:
----------
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:
---------
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.

"""


def longestPalindrome(s):
    """
    :type s: str
    :rtype: int
    """
    if len(s) == 1:  # if length of string is 1 then return 1
        return 1
    if s == s[-1:-len(s) - 1:-1]:  # if given string, and it's reversed version is same then return len(string)
        return len(s)
    s1 = list(s)  # convert the string into list
    s1 = set(s1)  # then convert into set to remove duplicates for next steps
    s1 = list(s1)  # again convert into list to perform operations (in set we can't)
    s2 = []
    s1.sort()
    # print(s1)
    length = 0
    for letter in s1:
        counts = s.count(letter)
        if counts >= 2:  # if letter(in converted list) have counts more than 2 in given string
            length += (counts // 2) * 2
        # if letter(in converted list) have counts less than 2 or have odd (but more than two) in given string
        if counts < 2 or counts % 2 != 0:
            s2.append(letter)
    if s2:
        length += 1  # in final check the new list s2 if the list have letters in it then add 1 to length. Because to make the longest palindrome
    return length  # return the longest palindrome's length


word = input()
print(longestPalindrome(word))
