# def findCount(n, arr, num, diff):
#     count=0
#     for i in range(n):
#         if(abs(arr[i]-num)<=diff):
#             count+=1
 
#     if count:
#         return count
#     return 0
 
# n=int(input("enter lenght od list:-"))
# arr=list(map(int,input("Enter list number:-").split()))
# num=int(input("find number:-"))
# diff=int(input("Diffrence of this number:-"))
# print(findCount(n, arr, num, diff))

n=[12,23,44,3,3,22,55]
num=int(input("find number:-"))
c=0
for i in range(len(n)):
    if (n[i]<=num):
        c+=1
if c:
    print(c)
else:
    print(0)