l=[1,2,2,3,1,1,1,1,2,3,4]
k=5

# brute-force approach 1
longest=0
for i in range(len(l)):
    for j in range(i+1,len(l)+1):
        total=0
        # generate each sub arary
        for n in range(i,j):
            total+=l[n]
        # checking the total of each sub array 
        if total==k:
            length=j-i
            longest=max(length,longest)
print(longest)



# Brute Force approach 2
longest=0
for i in range(len(l)):
    total=0
    for j in range(i,len(l)):
        total+=l[j]
        if total==k:
            longest=max(longest,j-i+1)
print(longest)



n = len(l) # size of the array
preSumMap = {}
Sum = 0
maxLen = 0
for i in range(n):
        # calculate the prefix sum till index i:
        Sum += l[i]
        # if the sum = k, update the maxLen:
        if Sum == k:
            maxLen = max(maxLen, i + 1)
        # calculate the sum of remaining part i.e. x-k:
        rem = Sum - k
        # Calculate the length and update maxLen:
        if rem in preSumMap:
            length = i - preSumMap[rem]
            maxLen = max(maxLen, length)
        # Finally, update the map checking the conditions:
        if Sum not in preSumMap:
            preSumMap[Sum] = i
print(maxLen)