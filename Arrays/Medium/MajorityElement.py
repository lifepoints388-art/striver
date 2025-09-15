# Majority Element (n/2)>2 times

nums=[1,2,3,2,2,3,2,3,1]
# Brute Force Approach
for num in nums:
    count=0
    for ele in nums:
        if num==ele:
            count+=1
    if count>len(nums)//2:
        print(num)
        break
else:
    print('none')

# Better Approach
# Hashing
d={}
for num in nums:
    if num not in d:
        d[num]=1
    else:
        d[num]+=1
for key,value in d.items():
    if value>len(nums)//2:
        print(key)
        break
else:
    print('none')

# Optimal
# Moores Voting Algorithm
count=0
for ele in nums:
    if count<=0:
        count=0
        num=ele
    elif num==ele:
        count+=1
    else:
        count-=1
# Verify
count=0
for ele in nums:
    if num==ele:
        count+=1
if count>len(nums)//2:
    print(num)
else:
    print('none')


# Optimal

count=0
num=None
for ele in nums:
    if count==0:
        count=1
        num=ele
    elif num==ele:
        count+=1
    else:
        count-=1
print(num)