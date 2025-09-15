# Sort an array of 0's, 1's and 2's
# Leet Code --> 75

# Brute-Force approach -->Any sortung technique 
# Use Merge sort --> TN=O(nlogn) SC=O(N)
# Using quick sort(O(n^2))
nums=[1,0,1,0,0,2,2,0,1,2,0]
def SortAnArray(nums):
    if len(nums)<=1:
        return nums
    pivote=nums[0]
    left=[ele for ele in nums[1:] if ele<pivote]
    right=[ele for ele in nums[1:] if ele>=pivote]
    return SortAnArray(left)+[pivote]+SortAnArray(right)
print(SortAnArray( nums))


# Better Approach
count0=0
count1=0
count2=0
for i in range(len(nums)):
    if nums[i]==0:
        count0+=1
    elif nums[i]==1:
        count1+=1
    else:
        count2+=1
for i in range(count0):
    nums[i]=0
for i in range(count0,count0+count1):
    nums[i]=1
for i in range(len(nums)-count2,len(nums)):
    nums[i]=2
print(nums)


# Optimal Approach
# Dutch National Flag Algorithm
# Rules:
"""
[0,low-1]->0's
[low,mid-1]->1's
[mid,high]->unsorted array
[high,n-1]->2's
initially low,mid are at 0 index and high at last index
"""
nums=[1,0,1,0,0,2,2,0,1,2,0]
low=0
mid=0
high=len(nums)-1
while mid<=high:
    if nums[mid]==0:
        nums[low],nums[mid]=nums[mid],nums[low]
        low+=1
        mid+=1
    elif nums[mid]==1:
        mid+=1
    elif nums[mid]==2:
        nums[mid],nums[high]=nums[high],nums[mid]
        high-=1
print(nums)