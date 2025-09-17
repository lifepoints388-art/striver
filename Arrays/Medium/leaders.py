# Leaders in an array



# Brute Force apprroach
def Leaders(arr):
    res=[]
    for i in range(len(arr)):
        leader=True
        for j in range(i+1,len(arr)):
            if arr[j]>arr[i]:
                leader=False
                break
        if leader:
            res.append(arr[i])
    return res
arr = [4, 7, 1, 0]
res=Leaders(arr)
print(res)


# optimal

def optimal(arr):
    res=[]
    max_ele=arr[-1]
    res.append(max_ele)
    ind=len(arr)-2
    while ind>=0:
        if arr[ind]>max_ele:
            max_ele=arr[ind]
            res.append(max_ele)
        ind-=1
    return res

res=optimal(arr)
print(res)