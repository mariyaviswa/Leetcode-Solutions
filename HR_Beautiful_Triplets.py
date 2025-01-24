"""
Given a sequence of integers a, a triplet (a[i], a[j], a[k]) is beautiful if:
1) i < j < k
2) a[j] - a[i] = a[k] - a[j] = d
Given an increasing sequence of integers and the value of d, count the number of beautiful triplets in the sequence.

Example
--------
arr [2, 2, 3, 4, 5]
d = 1
There are three beautiful triplets, by index: [i, j, k] = [0, 2, 3], [1, 2, 3], [2, 3, 4].
To test the first triplet, arr[j] — arr[i] = 3 - 2 = 1, arr[k] — arr[j] = 4 — 3 = 1.

Sample Input
------------
STDIN                  Function
7, 3                   arr[] size n = 7, d = 3
1 2 4 5 7 8 10         arr = [1,2,4,5,7,8,10]

Sample Output
-------------
3

Explanation
-----------

There are many possible triplets (arr[i], arr[j], arr[k]), but our only beautiful triplets are (1, 4, 7),
(4, 7, 10) and (2, 5, 8) by value
not index. Please see the equations below:
7 - 4 = 4 - 1 = 3 = d
10 - 7 = 7 - 4 = 3 = d
8 - 5 = 5 - 2 = 3 = d

Recall that a beautiful triplet satisfies the following equivalence relation: arr[j] — arr[i] = arr[k] — arr[j] = d where i < j < k.
"""


def beautifulTriplets(d, arr):
    # Write your code here
    count = 0
    for i in range(0, len(arr) - 2):
        for j in range(i + 1, len(arr) - 1):
            if arr[j] - arr[i] == d:
                for k in range(i + 2, len(arr)):
                    if arr[j] - arr[i] == d and arr[k] - arr[j] == d:
                        count += 1
    return count


first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
d = int(first_multiple_input[1])
arr = list(map(int, input().rstrip().split()))
print(beautifulTriplets(d, arr))
