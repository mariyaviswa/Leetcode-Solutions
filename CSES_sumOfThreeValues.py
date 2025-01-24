def findTarget(nums, target):

    for idx, val in enumerate(nums):
        nums[idx] = [val, idx]

    nums.sort()
    for i in range(0, len(nums)):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            if nums[left][0] + nums[right][0] + nums[i][0] == target:
                return sorted([nums[left][1] + 1, nums[right][1] + 1, nums[i][1] + 1])
            elif nums[left][0] + nums[right][0] + nums[i][0] < target:
                left += 1
            else:
                right -= 1
    return []


n, target = list(map(int, input().rstrip().split()))
nums = list(map(int, input().rstrip().split()))

res = findTarget(nums, target)

if res:
    print(res[0], res[1], res[2])
else:
    print("IMPOSSIBLE")
