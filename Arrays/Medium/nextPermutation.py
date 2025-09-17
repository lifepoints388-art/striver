
# Find the next permutation
# leet code ->31


def Reverse(arr,start,end):
    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
    return arr

def nextPermutation(arr):
    n=len(arr)
    # Step 1: Find the first decreasing element from the end
    i=n-2
    while i>=0 and arr[i]>=arr[i+1]:
        i-=1
    if i==-1:
        return Reverse(arr,0,n-1)
    # step2:find element larger than the arr[i]
    j=n-1   
    while arr[j]<arr[i]:
        j-=1
    # step3 : if found the element larger than arr[i] swap it with arr[j]
    arr[i],arr[j]=arr[j],arr[i]
    
    # step 4 :reverse the array from index i to end 
    return Reverse(arr,i+1,n-1)

arr = [2, 1, 5, 4, 3, 0, 0]
# res=nextPermutation(arr)
# print(res)