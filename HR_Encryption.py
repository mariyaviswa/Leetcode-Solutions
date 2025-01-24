import math

"""
An English text needs to be encrypted using the following encryption scheme
First, the spaces are removed from the text. Let L be the length of this text.
Then, characters are written into a grid, whose rows and columns have the following constraints:

 root(L) <= row <= column <= root(L), where x is floor function and x is ceil function
 
Example
-------

s = if man was meant to stay on the ground god would have given us roots
After removing spaces, the string is 54 characters long.root(54) is between 7 and 8, 
so it is written in the form of a grid with 7 rows and 8
columns.
    i f m a n w a s
    m e a n t t o s
    t a y o n t h e
    g r o u n d g o
    d w o u t d h a
    v e g i v e n u
    s r o o t s
• Ensure that rows X columns > L
• If multiple grids satisfy the above conditions, choose the one with the minimum area, i.e. rows x columns.
The encoded message is obtained by displaying the characters of each column, with a space between column texts. The encoded
message for the grid above is:
 imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn sseoau
 
Sample Input
------------
haveaniceday

Sample Output
-------------
hae and via ecy

Explanation
-----------
L = 12, root(12) is between 3 and 4.
Rewritten with 3 rows and 4 columns:

    have
    anic
    eday
"""


def encryption(s):
    # Write your code here
    length = len(s)
    square_root = math.sqrt(length)
    start = math.floor(square_root)
    end = math.ceil(square_root)
    splitted_words = []
    for i in range(0, length, end):
        splitted_words.append(s[i:i + end])
    result = ""
    for i in range(0, end):
        for j in range(0, len(splitted_words)):
            if i < len(splitted_words[j]):
                result += splitted_words[j][i]
        result += " "
    return result


sentence = input()
print(encryption(sentence))
