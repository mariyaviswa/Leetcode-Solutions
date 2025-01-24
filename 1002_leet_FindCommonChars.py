"""
1002. Find Common Characters
----------------------------

Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates).
You may return the answer in any order.
Example 1:
---------
Input: words = ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:
---------
Input: words = ["cool","lock","cook"]
Output: ["c","o"]
"""


def commonChars(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    common = []
    first_string = words[0]  # Take the first string in the list to check common letters
    k = 0
    while k < len(first_string):
        flag = True
        for i in range(1, len(words)):
            if first_string[k] not in words[i]:  # If the letters in each word then it assumes as common
                flag = False
        if flag:
            common.append(first_string[k])   # after assuming append to new list
            for j in range(1, len(words)):
                words[j] = words[j].replace(first_string[k], '', 1)  # after append then remove the common letter from each word
        k += 1
    return common


Words = ["bella", "label", "roller"]
print(commonChars(Words))
