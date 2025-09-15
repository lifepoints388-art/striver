# Check if Array Is Sorted and Rotated
# Leet Code -->1752
    
def Check(nums,count=0):
    n=len(nums)
    for ind in range(n):
        if nums[ind]>nums[(ind+1)%n]:
            count+=1
        if count>1:
            return False
    return True 

nums=[3,4,5,1,2]
print(Check(nums))
