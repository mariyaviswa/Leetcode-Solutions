"""
648. Replace Words
------------------

In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call
this word derivative. For example, when the root "help" is followed by the word "ful", we can form a derivative "helpful".

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces,
replace all the derivatives in the sentence with the root forming it. If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.

Return the sentence after the replacement.

Example 1:
---------
Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"

Example 2:
----------
Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c"
"""


def replaceWords(dictionary, sentence):
    """
    :type dictionary: List[str]
    :type sentence: str
    :rtype: str
    """
    sentence = sentence.split(" ")
    for i in range(0, len(sentence)):
        word = []
        for j in dictionary:
            if j in sentence[i]:  # first check the word from dictionary available in sentence[i] or not
                # Two-pointers 
                p1 = 0
                p2 = 0
                flag = True
                while p1 < len(j):
                    if j[p1] == sentence[i][p2]:  # check the word from dict and  sentence[i] have same char from index 0
                        p1 += 1
                        p2 += 1
                        continue
                    else:  # if not break
                        flag = False
                        break
                if flag:  # if flag only True then append all possible word from dict to word list
                    word.append(j)
        if len(word) == 1:
            sentence[i] = word[0]
        # To take the shortest length  from word list if list length > 1
        elif len(word) > 1:
            for k in range(1, len(word)):
                if len(word[0]) > len(word[k]):
                    word[0] = word[k]
            sentence[i] = word[0]  # finally append the shortest length word
    return ' '.join(sentence)


Dictionary = list(map(str, input().rstrip().split()))
Sentence = input()
print(replaceWords(Dictionary, Sentence))
