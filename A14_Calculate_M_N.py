m=int(input("enter m:-"))
n=int(input("enter n:-"))
s=0
for i in range(m , n):
    if i%3==0 and i%5==0:
        s+=i
print(s)