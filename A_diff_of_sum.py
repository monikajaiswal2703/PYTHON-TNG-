n=int(input("enter number N:-"))
m=int(input("enter number M:-"))
s1=0
s2=0
for i in range(m):
    if i%n==0:
        s1+=i
    else:
        s2+=i
print(abs(s2-s1))
