"""
1539. Kth Missing Positive Number
---------------------------------

Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array.



Example 1:
---------
Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.

Example 2:
---------
Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.

Using Brute force approach -> O(n) we can easily able to solve, but this binary search is efficient -> O(log(n))
"""


def findKthPositive(arr, k):
    # Time Complexity - O(log(n))
    # Space Complexity - O(1)
    n = len(arr)
    l, r = 0, n - 1

    while l <= r:
        mid = (r - l) // 2 + l
        missing = arr[mid] - (mid + 1)  # calculate how many missing values are there in that range

        if missing >= k:
            r = mid - 1
        else:
            l = mid + 1
    return l + k


arr = list(map(int, input().strip().split()))
k = int(input())
print("Kth missing: ", findKthPositive(arr, k))