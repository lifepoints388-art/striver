# Second Largest Element In Array
# Method 1:use sorting algorithm technique

# Mwthod 2: Optimal
l=[2,5,1,3,0]
first_max=l[0]
second_max=first_max
for ele in l:
    if ele>first_max:
        second_max=first_max
        first_max=ele 
    elif second_max<ele and ele<first_max:
        second_max=ele 
print(second_max)