strs = input()

maxi, count = 0, 1
for i in range(1, len(strs)):
    if strs[i] == strs[i-1]:
        count += 1
    else:
        maxi = max(count, maxi)
        count = 1
maxi = max(count, maxi)
print(maxi)