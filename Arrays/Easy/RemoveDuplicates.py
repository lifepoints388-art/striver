# Check if Array Is Sorted and Rotated
# Leet Code -->26
nums = [0,0,1,1,1,2,2,3,3,4]
# Brute Force
def Remove(nums):
    l=[]
    for ele in nums:
        if ele not in l:
            l.append(ele)
    for ind in range(len(l)):
        nums[ind]=l[ind]
    return nums

print(Remove(nums))

# using built in methods
print(len(set(nums)))

# Optimal
def RemoveDuplicates(nums):
    k=1
    for ind in range(1,len(nums)):
        if nums[ind]!=nums[ind-1]:
            nums[k]=nums[ind]
            k+=1
    return k,nums
    

# print(RemoveDuplicates(nums))
