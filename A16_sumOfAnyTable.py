n=int(input("enter the number:-"))
s=0
for j in range(1,11):
    a=j*n
    s+=a
    print(a,end=", ")
print("\n",s)