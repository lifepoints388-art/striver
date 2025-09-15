# leet code -->136
nums= [4,1,2,1,2]
# brute force
# TC -> O(n^2)
# SC -> O(1)
for num in nums:
    count=0
    for ele in nums:
        if num==ele:
            count+=1
    if count==1:
        print(num)
        break

# better approach
# TC -> O(n)
# SC -> O(n)
res={}
for ele in nums:
    if ele not in res:
        res[ele]=1
    else:
        res[ele]+=1
for key,value in res.items():
    if value==1:
        print(key)
        break


# optimal
# TC -> O(n)
# SC -> O(1)
res=nums[0]
for ind in range(1,len(nums)):
    res^=nums[ind] 
print(res)

# without using in operator
nums=[1,22,22,3,3,4,4]
d={}
for ele in nums:
    found=False
    for key in d:
        if key==ele:
            d[ele]+=1 
            found=True
            break
    if not found:
        d[ele]=1
print(d)