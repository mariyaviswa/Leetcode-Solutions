"""
Count Subarrays with given XOR
------------------------------

Given an array of integers arr[] and a number k, count the number of subarrays having XOR of their elements as k.

XOR operations
---------------
        A   B   A⊕B

        1   1    0
        1   0    1
        0   1    1
        0   0    0

if both same, result will be zero
else 1


Examples:
--------
Input: arr[] = [4, 2, 2, 6, 4], k = 6
Output: 4
Explanation: The subarrays having XOR of their elements as 6 are [4, 2], [4, 2, 2, 6, 4], [2, 2, 6], and [6]. Hence, the answer is 4.

Input: arr[] = [5, 6, 7, 8, 9], k = 5
Output: 2
Explanation: The subarrays having XOR of their elements as 5 are [5] and [5, 6, 7, 8, 9]. Hence, the answer is 2.

Note :
------
  This problem same as --> subarray sum equals k.
"""


def subarrayXor(arr, k):

    store = {0: 1}
    curr = 0
    res = 0

    for num in arr:
        curr ^= num
        if curr ^ k in store:
            res += store.get(curr ^ k, 0)
        store[curr] = store.get(curr, 0) + 1
    return res


nums = list(map(int, input().rstrip().split()))
k = int(input())
res = subarrayXor(nums, k)
print("Total subarrays: ", res)
