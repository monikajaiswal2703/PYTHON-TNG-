# lenght=int(input("Enter lenght:-"))
arr=list(map(int,input("enter the list value:-").split()))
even_a=[]
odd_a=[]
for i in range(len(arr)):
    if i % 2 ==0: # i is a index value of arr list
        even_a.append(arr[i])# append even index value of list
    else:
        odd_a.append(arr[i]) # append odd index value of list
even_a=sorted(even_a) # sorting the arr like 1 2 3
odd_a=sorted(odd_a) #sorting the arr like 1 2 3
print(even_a)
print(odd_a)
print(even_a[len(even_a)-2] + odd_a[len(odd_a)-2])
# m=even_a[len(even_a)-2]
# n=odd_a[len(odd_a)-2]
# print(m+n)