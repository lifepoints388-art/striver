# Longest successive sub sequence in an array
nums= [100, 200, 1, 3, 4, 2]


# Brute force
def LongestSubsequence(nums):
    longest=1
    n=len(nums)
    for i in range(n):
        num=nums[i]
        count=1
        while num+1 in nums:
            num+=1
            count+=1
        if count>longest:
            longest=count
            count=0
    return longest

res=LongestSubsequence(nums)
print(res)



# Better
def Better(nums):
    nums.sort()
    longest=1
    count=0
    lastSmaller=nums[0]-1
    for i in range(len(nums)):
        if nums[i]-1==lastSmaller:
            count+=1
            lastSmaller=nums[i]
        elif nums[i]!=lastSmaller:
            lastSmaller=nums[i]
            count=1
        longest=max(longest,count)
    return longest
nums= [100, 200, 1, 3, 4, 2]
res=Better(nums)
print(res)


# Optimal

def optimal(nums):
    s=set(nums)
    count=0
    longest=1
    for ele in nums:
        if ele-1 not in s:
            count=1
            val=ele+1
            while val in s:
                count+=1
                val+=1
        longest=max(longest,count)
    return longest

nums= [100, 200, 1, 3, 4, 2]
res=optimal(nums)
print(res)