# Rotate Array -->189

nums=[1,2,3,4,5,6,7]
k=3
k=k%len(nums)
# Method 1: Using Slicing
# nums[:]=nums[-k:]+nums[:-k]
print(nums)

# Method 2:using function to rotate array

# step 1: reverse entore array
# [7,6,5,4,3,2,1]
# step 2: reverse first k elements
# [5,6,7,4,3,2,1]
# step 3: reverse n-1 elements
# [5,6,7,1,2,3,4]

def Reverse(start,end):
    while start<end:
        nums[start],nums[end]=nums[end],nums[start]
        start+=1
        end-=1
    
n=len(nums)
Reverse(0,n-1)
Reverse(0,k-1)
Reverse(k,n-1)
print(nums)