"""
443. String Compression
-----------------------

Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:
    If the group's length is 1, append the character to s.
    Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars.
Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.
You must write an algorithm that uses only constant extra space.

Example 1:
----------
Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

Example 2:
----------
Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.

Example 3:
----------
Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
"""


def compress(chars):
    """
    :type chars: List[str]
    :rtype: int
    """
    if len(chars) == 1:  # if the length of the list is 1
        return 1
    # else this case
    s = ""  # create a new empty string
    count = 1
    for char in range(1, len(chars)):
        # if current char != prev char then append the prev char to string along with its length if greater than 1
        if chars[char] != chars[char - 1]:
            s += chars[char - 1]
            if count > 1:
                s += str(count)
                count = 1
        else:  # count while chars[char] != chars[char - 1]
            count += 1
    # finally append the last distinct char in given list to string along with its length if greater than 1
    s += chars[len(chars) - 1]
    if count > 1:
        s += str(count)
    # return the given char list with modify the value as in string in-place
    for i in range(0, len(s)):
        chars[i] = s[i]
    return len(chars[:len(s)])  # return the compressed string length


characters = list(map(str, input().rstrip().split()))
print(compress(characters))
