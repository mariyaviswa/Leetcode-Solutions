"""
769. Max Chunks To Make Sorted
------------------------------

You are given an integer array arr of length n that represents a permutation of the integers in the range [0, n - 1].

We split arr into some number of chunks (i.e., partitions), and individually sort each chunk.
After concatenating them, the result should equal the sorted array.

Return the largest number of chunks we can make to sort the array.



Example 1:
---------
Input: arr = [4,3,2,1,0]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.

Example 2:
---------
Input: arr = [1,0,2,3,4]
Output: 4
Explanation:
We can split into two chunks, such as [1, 0], [2, 3, 4].
However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.
"""


from sortedcontainers import SortedList


def maxChunksToSorted(arr):
    # Time Complexity - O(n)
    # Space Complexity - O(n)
    count = 0
    keepTrack = SortedList()
    for idx, num in enumerate(arr):
        keepTrack.add(num)

        if idx == keepTrack[-1]:  # whenever index equal to the last element in the sorted list we can increase our chunks to maximize
            count += 1
        """
        Using max-function method
        ----------------
        max = 0
        max = max(max, num)
        if max == idx:
            count += 1
        
        Using calculate the difference 
        ------------------------------
        
        diff += num -  idx
        if diff == 0:
            count += 1 
        """
    return count


nums = list(map(int, input().rstrip().split()))
print("Max Chunks: ", maxChunksToSorted(nums))
