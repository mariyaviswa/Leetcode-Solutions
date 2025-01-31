"""
1122. Relative Sort Array
-------------------------

Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.
Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.
Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.

Example 1:
---------
Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]

Example 2:
---------
Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
Output: [22,28,8,6,17,44]
"""


def relativeSortArray(arr1, arr2):
    """
    :type arr1: List[int]
    :type arr2: List[int]
    :rtype: List[int]
    """
    values = []
    for i in arr2:
        count = arr1.count(i)  # count each value's count  in arr1
        j = 1
        while j <= count:
            values.append(i)
            arr1.remove(i)
            j += 1
    arr1.sort()  # remains in arr1 sort normal ascending order
    values += arr1
    return values


array1 = list(map(int, input().rstrip().split()))
array2 = list(map(int, input().rstrip().split()))
print(relativeSortArray(array1, array2))
