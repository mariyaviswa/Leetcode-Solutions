"""
1769. Minimum Number of Operations to Move All Balls to Each Box
----------------------------------------------------------------

problem link - https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

You have n boxes. You are given a binary string boxes of length n, where boxes[i] is '0' if the ith box is empty,
and '1' if it contains one ball.

In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j if abs(i - j) == 1.
Note that after doing so, there may be more than one ball in some boxes.

Return an array answer of size n, where answer[i] is the minimum number of operations needed to move all the balls to the ith box.

Each answer[i] is calculated considering the initial state of the boxes.



Example 1:

Input: boxes = "110"
Output: [1,1,3]
Explanation: The answer for each box is as follows:
1) First box: you will have to move one ball from the second box to the first box in one operation.
2) Second box: you will have to move one ball from the first box to the second box in one operation.
3) Third box: you will have to move one ball from the first box to the third box in two operations,
and move one ball from the second box to the third box in one operation.
"""


def minOperations(boxes):
    # Time Complexity - O(n)
    # Space Complexity - O(n)

    n = len(boxes)
    ones = 0
    prefix = 0
    ans = [0] * len(boxes)

    for i in range(0, n):
        ans[i] += prefix
        if boxes[i] == '1':
            ones += 1
        prefix += ones

    suffix = 0
    ones = 0
    for j in range(n - 1, -1, -1):
        ans[j] += suffix
        if boxes[j] == '1':
            ones += 1
        suffix += ones
    return ans


"""
        # Time Complexity - O(n^2)
        # Space Complexity - O(n)
        
        ones = 0
        prefix = 0
        ans = [0] * len(boxes)

        for i in range(0, len(boxes)):
            res = 0
            res += prefix
            for j in range(i+1, len(boxes)):
                if boxes[j] == '1': res += abs(j - i)
            if boxes[i] == '1':
                ones += 1
            prefix += ones
            ans[i] = res

        return ans

"""

nums = list(map(int, input().rstrip().split()))
print("Minimum Operations to Move All Balls: ", minOperations(nums))
