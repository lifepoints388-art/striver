# Move all zeros to end --->leet code 283


# method 1
nums=[0,1,0,3,12]
pos=0
for ind in range(len(nums)):
    if nums[ind]!=0:
        nums[pos],nums[ind]=nums[ind],nums[pos]
        pos+=1
print(nums)


# Method 2
nums=[0,1,0,3,12]
for ele in nums:
    if ele==0:
        nums.append(ele)
        nums.remove(ele)
print(nums)