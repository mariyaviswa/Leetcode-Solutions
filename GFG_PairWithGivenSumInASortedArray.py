"""
Pair with given sum in a sorted array
-------------------------------------

problem link - https://www.geeksforgeeks.org/problems/pair-with-given-sum-in-a-sorted-array4940/1

You are given an integer target and an array arr[]. You have to find number of pairs in arr[] which sums up to target. It is given that the elements of the arr[] are in sorted order.
Note: pairs should have elements of distinct indexes.

Examples :
----------
Input: arr[] = [-1, 1, 5, 5, 7], target = 6
Output: 3
Explanation: There are 2 pairs which sum up to 6 : {1, 5}, {1, 5} and {-1, 7}.

Input: arr[] = [1, 1, 1, 1], target = 2
Output: 6
Explanation: There are 6 pairs which sum up to 2 : {1, 1}, {1, 1}, {1, 1}, {1, 1}, {1, 1} and {1, 1}.

Input: arr[] = [-1, 10, 10, 12, 15], target = 125
Output: 0
Explanation: There is no such pair which sums up to 4.
"""


def countPairs(arr, target):
    # Complete the function
    # Time Complexity - O(n)
    # Space Complexity - O(1)
    left, right = 0, len(arr) - 1
    res = 0

    while left < right:
        if arr[left] + arr[right] < target:
            left += 1
        elif arr[left] + arr[right] > target:
            right -= 1
        else:
            cnt1 = 0
            cnt2 = 0
            elem1, elem2 = arr[left], arr[right]

            while left <= right and arr[left] == elem1:
                left += 1
                cnt1 += 1
            while left <= right and arr[right] == elem2:
                right -= 1
                cnt2 += 1

            if elem1 == elem2:
                res += (cnt1 * (cnt1 - 1)) // 2

            else:
                res += cnt1 * cnt2

    return res


arr = list(map(int, input().strip().split()))
target = int(input())
ans = countPairs(arr, target)
print("Total pairs: ", ans)