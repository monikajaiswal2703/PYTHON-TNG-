a=int(input())
b=int(input())
c=0
d=0
for i in range(1,b+1):
    if i%a==0:
        c+=i
    else:
        d+=i
print(c)
print(d)
print(d-c)
