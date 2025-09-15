# Largest Element In Array
# Method 1:use sorting algorithm technique 


# Method 2:optimal
l=[2,5,1,3,0]
largest=l[0]
for ele in l:
    if ele>largest:
        largest=ele
print(largest)