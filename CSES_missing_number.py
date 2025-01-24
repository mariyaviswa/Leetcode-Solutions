n = int(input())
nums = list(map(int, input().rstrip().split()))

totalSum = (n * (n+1)) // 2
currSum = 0
for i in range(0, len(nums)):
    currSum += nums[i]

missing = totalSum - currSum
print(missing)