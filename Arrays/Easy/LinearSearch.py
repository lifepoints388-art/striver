# Linear search
# if given number is present in the array return the index otherwise return -1
nums=[1,2,3,4,5,6,7]
num=6
def LinearSearch(nums,num):
    for ind in range(len(nums)):
        if nums[ind]==num:
            return ind 
    return -1
print(LinearSearch(nums,num))