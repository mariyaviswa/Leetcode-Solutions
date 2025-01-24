"""
Count distinct elements in every window
---------------------------------------

Given an integer array arr[] and a number k. Find the count of distinct elements in every window of size k in the array.

Examples:
--------
Input: arr[] = [1, 2, 1, 3, 4, 2, 3], k = 4
Output:  [3, 4, 4, 3]
Explanation: Window 1 of size k = 4 is 1 2 1 3. Number of distinct elements in this window are 3.
Window 2 of size k = 4 is 2 1 3 4. Number of distinct elements in this window are 4.
Window 3 of size k = 4 is 1 3 4 2. Number of distinct elements in this window are 4.
Window 4 of size k = 4 is 3 4 2 3. Number of distinct elements in this window are 3.

Input: arr[] = [4, 1, 1], k = 2
Output: [2, 1]
Explanation: Window 1 of size k = 2 is 4 1. Number of distinct elements in this window are 2.
Window 2 of size k = 2 is 1 1. Number of distinct elements in this window is 1.
Input: arr[] = [1, 1, 1, 1, 1], k = 3
Output: [1, 1, 1]
"""


def countDistinct(arr, k):
    # Code here
    # Time Complexity - O(n)
    # Space Complexity - O(n)
    nums = {}

    st = 0
    ed = 0

    for i in range(0, len(arr)):
        nums[arr[i]] = nums.get(arr[i], 0) + 1

        ed = i + 1  # Update the window ending position

        # If the window size reached k
        if ed - st == k:
            temp = arr[st]
            arr[st] = len(nums)
            # Check the previous window value present in the current window
            # Then decrease the value count, so can avoid duplicates
            if temp in nums:
                nums[temp] -= 1
                # if the value count 0 remove from the dictionary
                if not nums[temp]:
                    del nums[temp]
            st += 1  # Update the window starting position
    return arr[:st]


nums = list(map(int, input().split()))
window_size = int(input())
res = countDistinct(nums, window_size)
print("The all distinct elements frm each window: ", res)