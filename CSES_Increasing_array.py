n = int(input())

nums = list(map(int, input().rstrip().split()))

maxCount = 0

for i in range(1, len(nums)):
    if nums[i] < nums[i-1]:
        maxCount += nums[i-1] - nums[i]
        nums[i] += nums[i-1] - nums[i]
print(maxCount)