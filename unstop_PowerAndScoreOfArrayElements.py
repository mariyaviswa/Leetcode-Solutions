"""
Power and Score of Array Elements
---------------------------------

Problem Statement
-----------------
Given an array arr[] (0-based indexed) of integers of size N, define the power of the integer at index i as follows:

Let:
----

a be the second minimum integer among all integers with indices less than i .
b be the second minimum integer among all integers with indices greater than i.
The power of the integer at index i is defined as:
                  max(arr[i] - a, arr[i] - b).

The score of the array arr is defined as the sum of powers for all integers in the array.
Print the score of the array arr.

Note: If there are less than equal to one element before or after the index i,
then consider the second minimus as INT_MAX.

Input Format
The first line contains an integer N which denotes the size of the array.

The second line contains N space-separated integers denoting the elements of the array arr[].

Output Format
-------------
Print an integer denoting the score of the array.

Constraints
-----------
1 <= N <= 10^5

1 <= Arr[i] <= 10^6

Sample Testcase 0
-----------------
Testcase Input
--------------
5
4 7 1 8 3

Testcase Output
---------------
2

Explanation
-----------
Index 0 (arr[0] = 4):
Before: INT_MAX (no elements).
After: Second minimum in [7, 1, 8, 3] = 3.
Score: max(4 - INT_MAX, 4 - 3) = 1.

Index 1 (arr[1] = 7):
Before: Second minimum in [4] = INT_MAX.
After: Second minimum in [1, 8, 3] = 3.
Score: max(7 - INT_MAX, 7 - 3) = 4.


Index 2 (arr[2] = 1):
Before: Second minimum in [4, 7] = 7.
After: Second minimum in [8, 3] = 8.
Score: max(1 - 7, 1 - 8) = -6.


Index 3 (arr[3] = 8):
Before: Second minimum in [4, 7, 1] = 4.
After: INT_MAX (no elements).
Score: max(8 - 4, 8 - INT_MAX) = 4.


Index 4 (arr[4] = 3):
Before: Second minimum in [4, 7, 1, 8] = 4.
After: INT_MAX (no elements).
Score: max(3 - 4, 3 - INT_MAX) = -1.


Total Score: 1 + 4 - 6 + 4 - 1 = 2.
"""


def computeScore(arr):
    """
    Write your logic here.
    Parameters:
        arr (list): List of integers
    Returns:
        int: Computed result based on the problem statement
    """
    prefix = [0] * len(arr)  # for storing the all prefix second minimum
    suffix = [0] * len(arr)  # for storing the all suffix second minimum

    prefix[0] = 2147483647  # int maximum value (Because oth and 1st array won't have second minimum)
    suffix[-1] = 2147483647  # int maximum value (Because last and last before array won't have second minimum)

    first = arr[0]
    second = 2147483647
    for i in range(1, len(arr)):
        prefix[i] = second
        # Update the 1st and 2nd minimum for each index so far seen
        if arr[i] < first:
            second = first
            first = arr[i]
        elif arr[i] < second and arr[i] > first:
            second = arr[i]

    f1 = arr[-1]
    s1 = 2147483647
    for j in range(len(arr) - 2, -1, -1):
        suffix[j] = s1
        # Update the 1st and 2nd minimum for each index so far seen
        if arr[j] < f1:
            s1 = f1
            f1 = arr[j]
        elif arr[j] < s1 and arr[j] > f1:
            s1 = arr[j]

    score = 0
    for i in range(0, len(arr)):
        score += max(arr[i] - prefix[i], arr[i] - suffix[i])
    # print(prefix)
    # print(suffix)
    return score


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])  # First input is the integer n
    arr = list(map(int, data[1:]))  # Remaining input is the array of integers

    # Call user logic function and print the output
    result = computeScore(arr)
    print(result)


if __name__ == "__main__":
    main()