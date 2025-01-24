def productExceptSelf(nums):
    # Time Complexity - O(n)
    # Space Complexity - O(1) since the output array is excluded from space analysis.
    n = len(nums)
    res = [1] * n

    prefix = 1
    for i in range(0, len(nums)):
        res[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for j in range(len(nums) - 1, -1, -1):
        res[j] *= postfix
        postfix *= nums[j]

    return res


arr = list(map(int, input().split()))
ans = productExceptSelf(arr)
print("The result array: ", ans)

"""
Using Extra-Space for prefix and postfix
----------------------------------------
        #code here
        # Time Complexity - O(n)
        # Space Complexity - O(n)
        
        prefix = [1 for _ in range(len(arr)+1)]
        postfix = [1 for _ in range(len(arr)+1)]
        
        for i in range(0, len(arr)):
            prefix[i+1] = prefix[i] * arr[i]
            
        for i in range(len(arr)-1, -1, -1):
            postfix[i] = postfix[i+1] * arr[i]
        
        for i in range(0, len(arr)):
            arr[i] = prefix[i] * postfix[i+1]
        return arr

Using Division method
---------------------
        #code here
        # Time Complexity - O(n)
        # Space Complexity - O(1) since the output array is excluded from space analysis.
        
        prod, zero_count = 1, 0
        
        for i in range(0, len(arr)):
            if arr[i]:
                prod *= arr[i]
            else:
                zero_count += 1
        if zero_count > 1: return [0] * len(arr)
        
        res = [0] * len(arr)
        for i in range(0, len(arr)):
            if zero_count == 1:
                if arr[i] == 0: res[i] = prod
            else:
                res[i] = prod // arr[i]
        return res

"""