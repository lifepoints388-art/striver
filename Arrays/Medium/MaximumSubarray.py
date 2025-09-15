# Maximum Subarray Sum in an Array
import sys


# Brute Force Approach
def Max_Sum(arr,n):
    maxsum=-sys.maxsize-1
    for i in range(n):
        for j in range(i+1,n+1):
            Sum=0
            for k in range(i,j):
                Sum+=arr[k]
            if Sum>maxsum:
                maxsum=Sum
    return maxsum
arr=[-2,1,-3,4,-1,2,1,-5,4]
n=len(arr)
res=Max_Sum(arr,n)
print(res)


# Better Approach

def Max_sum_Better(arr,n):
    maxsum=-sys.maxsize-1
    for i in range(n):
        Sum=0
        for j in range(i,n):
            Sum+=arr[j]
            if Sum>maxsum:
                maxsum=Sum
    return maxsum
arr=[-2,1,-3,4,-1,2,1,-5,4]
n=len(arr)
res=Max_sum_Better(arr,n)
print(res)


# Optimal Approach
# Kadene's Algorithm
def Kadenes(arr,n):
    maxsum=-sys.maxsize-1
    total=0
    for i in range(n):
        # if total==0:
        #     start=i
        total+=arr[i]
        if total>maxsum:
            maxsum=total
            # arrStart=start 
            # arrEnd=i 
        if total<0:
            total=0
    return maxsum,"arr[arrStart:arrEnd+1]"

arr=[-2,1,-3,4,-1,2,1,-5,4]
n=len(arr)
res=Kadenes(arr,n)
print(res)