"""
974. Subarray Sums Divisible by K  (as problem 523)
---------------------------------

Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

A subarray is a contiguous part of an array.

Example 1:
---------
Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

Example 2:
---------
Input: nums = [5], k = 9
Output: 0
"""


def subarraysDivByK(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    """
    # Brute force approach
    if len(nums) == 1:
        if nums[0] % k == 0:
            return 1
        else:
            return 0
    count = 0
    sub = 0
    for i in range(0, len(nums)):
        count = 0
        Sum = 0
        for j in range(i, len(nums)):
            Sum += nums[j]
            if Sum % k == 0:
                sub += 1
    return sub
    """
    dictionary = {0: 1}
    Sum = 0
    sub_tot = 0
    for num in nums:
        Sum += num  # prefix_sum
        remain = Sum % k  # modulo the prefix sum extract the remainder
        if remain in dictionary:  # check the remain in dictionary if in
            dictionary[remain] += 1  # then increase the key's value by 1
            sub_tot += dictionary[remain] - 1  # add the key's value after incrementing and subtract 1 in sub_tot
        else:
            dictionary[remain] = 1  # check the remain in dictionary if not in assign the remain key value  1
    return sub_tot  # return the sub-tot


Nums = list(map(int, input().rstrip().split()))
K = int(input())
print(subarraysDivByK(Nums, K))
