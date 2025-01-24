"""
846. Hand of Straights
----------------------

Alice has some number of cards, and she wants to rearrange the cards into groups so that each group is of size groupSize,
and consists of groupSize consecutive cards.
Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize,
return true if she can rearrange the cards, or false otherwise.

Example 1:
---------
Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]

Example 2:
----------
Input: hand = [1,2,3,4,5], groupSize = 4
Output: false
Explanation: Alice's hand can not be rearranged into groups of 4.

"""


def isNStraightHand(hand, groupSize):
    """
    :type hand: List[int]
    :type groupSize: int
    :rtype: bool
    """
    if len(hand) % groupSize != 0:  # if we can't form the groups(with consecutive order) with size of groupSize
        return False
    group = int(len(hand) / groupSize)  # total groups with groupSize
    if len(hand) % group == 0:  # if we can form the groups(with consecutive order) with size of groupSize
        hand.sort()
        for i in range(0, int(len(hand) / groupSize)):
            vals = []
            prev = hand[0]  # while starting assign the first value in prev variable for the below operation
            # print(prev)
            hand.remove(hand[0])  # then remove prev from hand list
            vals.append(prev)  # store each groups in vals list
            j = 1
            while j < groupSize:  # check can form groups or not with consecutive order
                if (prev + 1) in hand:
                    prev = prev + 1
                    vals.append(prev)
                    hand.remove(prev)
                else:
                    return False  # can't, return False
                j += 1
            # print(vals)
    return True


Hand = list(map(int, input().rstrip().split()))
GroupSize = int(input())
print(isNStraightHand(Hand, GroupSize))
