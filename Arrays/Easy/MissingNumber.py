nums=[0,1,2,3,4,6]
n=len(nums)
# brute force
for num in range(n):
    if num not in nums:
        print(num)
        break



actual_sum=0
for num in nums:
    actual_sum+=num
expected_sum=n*(n+1)//2
print(expected_sum-actual_sum)



# optimal
missing=len(nums)
for i,num in enumerate(nums):
    missing^=i^num 
print(missing)