"""
383. Ransom Note
----------------

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and
false otherwise.
Each letter in magazine can only be used once in ransomNote.
Example 1:
---------
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
----------
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
----------
Input: ransomNote = "aa", magazine = "aab"
Output: true
"""


def canConstruct(ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    flag = True
    new_string = list(magazine)  # convert the magazine into list
    for letter in ransomNote:
        if letter in new_string:  # check letter(from ransomNote) in new_string is available or not
            new_string.remove(letter)  # if there then remove from new_string
        else:
            flag = False
    if flag:
        return True
    else:
        return False


ransomeNote = input()
Magazine = input()
print(canConstruct(ransomeNote, Magazine))
