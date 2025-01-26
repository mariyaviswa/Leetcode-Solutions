"""
2. Add Two Numbers
------------------

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    # Time Complexity - O(n)
    # Space Complexity - O(1)
    dummy = curr = ListNode()

    carry = 0

    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        val = (v1 + v2 + carry) % 10
        carry = (v1 + v2 + carry) // 10

        curr.next = ListNode(val)
        curr = curr.next

        l1 = l1.next if l1 is not None else None
        l2 = l2.next if l2 is not None else None
    return dummy.next
