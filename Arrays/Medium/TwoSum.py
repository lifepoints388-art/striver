# Two sum problem


# Brute Force Approach
nums=[2,7,5,9,11,13]
target=14
for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
            print(i,j)



# Better
res={}
for i,num in enumerate(nums):
    r=target-num
    if r in res:
        print(res[r],i)
        break
    res[num]=i 


# Optimal

nums.sort()
left=0
right=len(nums)-1
while left<right:
    total=nums[left]+nums[right]
    if total==target:
        print('YES')
        break
    elif total>target:
        right-=1
    else:
        left+=1
