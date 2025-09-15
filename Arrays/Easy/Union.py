# Union of two sorted arrays

arr1=[1,2,3,4,5,11]
arr2=[2,2,3,3,4,4,5,6,7,8,9,9,10]

s=set(arr1).union(set(arr2))
print(s)


u=set(arr1)|set(arr2)
res={val:val for val in u}
print(list(res))

l=[]
for ele in arr1:
    if ele not in l:
        l.append(ele)
for ele in arr2:
    if ele not in l:
        l.append(ele)
print(l)

for ind in range(1,len(l)):
    for ind2 in range(ind,0,-1):
        if l[ind2]<l[ind2-1]:
            l[ind2],l[ind2-1]=l[ind2-1],l[ind2]
print(l)

l=[]
for ele in arr1+arr2:
    if ele not in l:
        l.append(ele)
print(l)