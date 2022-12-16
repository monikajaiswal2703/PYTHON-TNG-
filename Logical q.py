# "maximum in list"
# a=[8,4,5,3,2,6,56,9,1,97]
# m=0
# i=0
# while i<len(a):
#     if a[i]<m:
#         m=a[i]
#         b=i
#     i+=1
# print(m,b)

# "minimum in list"
# a=[8,4,5,3,2,6,56,9,1,97]
# m=len(a)
# i=0
# while i<len(a):
#     if a[i]<m:
#         m=a[i]
#         b=i
#     i+=1
# print(m,b)

# def sum_lis(a,b):
#     i=0
#     s=0
#     j=1
#     while i<len(a):
#         s=s+a[i]*b[-i-1]
#         i+=1
#     print(s)
# a=[1,2,3,33,44,22]
# b=[2,33,11,4,6,7]
# sum_lis(a,b)


# import datetime
# # print("Current date and time: " , datetime.datetime.now())
# # print("Current year: ", datetime.date.today().strftime("%Y"))
# # print("Month of year: ", datetime.date.today().strftime("%B"))
# # print("Week number of the year: ", datetime.date.today().strftime("%W"))
# # print("Weekday of the week: ", datetime.date.today().strftime("%w"))
# # print("Day of year: ", datetime.date.today().strftime("%j"))
# # print("Day of the month : ", datetime.date.today().strftime("%d"))
# # print("Day of week: ", datetime.date.today().strftime("%A"))

# time = "Jan 1 2014 2:43 PM"
# print(datetime.datetime.strptime(time,"%b %d %Y %H:%M %p"))
# t=int(input())
# for T in range(t):
#     a=list(map(int,input().split()))
#     a.sort()
#     print(a[-2])
    
# t=int(input())
# for T in range(t):
#     a,b=map(int,input().split())
print(0*4)