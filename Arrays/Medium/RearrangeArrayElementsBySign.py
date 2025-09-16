# Rearranging the array elements by sign
# if positive and negative elements are same in an array
# Brute-Force approach
def Brute_Force(nums):
    pos=[]
    neg=[]
    for ele in nums:
        if ele>0:
            pos.append(ele)
        else:
            neg.append(ele)
    ind=0
    while ind<len(pos):
        nums[ind*2]=pos[ind]
        ind+=1
    ind=1
    while ind<len(neg)+1:
        nums[ind*2-1]=neg[ind-1]
        ind+=1
nums=[1,2,-4,-5]
Brute_Force(nums)
print(nums)

# Better approach
def Better(nums):
    res=[0]*len(nums)
    pos=0
    neg=1
    for ele in nums:
        if ele>0:
            res[pos]=ele
            pos+=2
        else:
            res[neg]=ele
            neg+=2
    return res
res=Better(nums)
print(res)

# if positive and negative elements are not same in an array


def SecondVariety(nums):
    pos=[]
    neg=[]
    for ele in nums:
        if ele>0:
            pos.append(ele)
        else:
            neg.append(ele)
    ind=0
    if len(pos)<len(neg):
        while ind<len(pos):
            nums[ind*2]=pos[ind]
            nums[(ind+1)*2-1]=neg[ind]
            ind+=1
        # while ind<len(neg):
        #     nums[ind+2]=neg[ind]
        #     ind+=1
        ind=len(pos)*2
        i=len(neg)
        while i<len(pos):
            nums[ind]=pos[i]
            i+=1
            ind+=1
    else:
        while ind<len(neg):
            nums[ind*2]=pos[ind]
            nums[(ind+1)*2-1]=neg[ind]
            ind+=1
        # while ind<len(pos):
        #     nums[ind+2]=pos[ind]
        #     ind+=1
        ind=len(neg)*2
        i=len(neg)
        while i<len(pos):
            nums[ind]=neg[i]
            i+=1
            ind+=1
    return nums
nums=[1,-2,3,-4,-5,-6]
SecondVariety(nums)
print(nums)