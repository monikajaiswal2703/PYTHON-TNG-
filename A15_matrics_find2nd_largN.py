num=int(input("enter size of arr:-"))
arr=list(map(int,input("enter num:-").split()))
i=0
even=[]
odd=[]
while i<len(arr):
    if i%2==0:
        even.append(arr[i])
    else:
        odd.append(arr[i])
    i+=1
c=even+odd
c=sorted(c)
n=c[len(c)-2]
print(n)