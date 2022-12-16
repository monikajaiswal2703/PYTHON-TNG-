str=input("enter string:-")
a=[False]*128
is_uniqe=True
for i in str:
    if len(str)>128:
        is_uniqe=False
    val=ord(i)
    if a[val]:
        is_uniqe = False
    a[val]=True
if is_uniqe:
    print("good")
else:
    print("bad")

# a=ord("a")
# print(a)