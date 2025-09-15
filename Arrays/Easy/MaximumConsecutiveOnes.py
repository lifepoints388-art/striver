nums=[1,1,1,1,0,1,0,1,1,1,0,1,1,1,1,1,1]
count=0
max_count=0
for num in nums:
    if num==1:
        count+=1
    else:
        count=0
    max_count=max(count,max_count)
print(max_count)