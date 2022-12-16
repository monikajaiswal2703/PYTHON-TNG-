# Str1 = "WElcome"
# low=[]
# upp=[]
# for i in Str1:
#     if i.islower()==True:
#         low.append(i)
#     else:
#         upp.append(i)
# a=low+upp
# b=" ".join(a)
# print(b)

# def sm():
#     n=int(input("enter no:"))
#     n1=int(input("enter 2nd no:"))
#     return n+n1
# print(sm())

# Str1 = "Apple"
# d1={}
# for i in Str1:
#     value=Str1.count(i)
#     d1[i]=value
# print(d1)

# str2='monikajaiswal'
# d={}
# c=0
# for i in str2:
#     c=str2.count(i)
#     d[i]=c
# print(d)

# str1 = "Emma-is-a-data-scientist"
# a=str1.split("-")
# print(a)
# for i in a:
#    print(i)

# def maximum(a):
#     print(max(a))
# a=[4,55,66,77,88,89,444,12,22]
# maximum(a)

# "2 nd way"
# def m(a):
#     m1=0
#     for i in a:
#         if m1<=i:
#             m1=i
#     return m1
# a=[4,55,66,77,88,89,3445,444,44]
# print(m(a))

# def d(a):
#     if a==1:
#         return 1
#     else:
#         return a*d+(a-1)
# a=int(input("enter the nomber:"))
# print(d(a))

# def f():
#     num=int(input("enter the number"))
#     fac=1
#     i=1
#     while i<=num:
#         fac=fac*i
#         i+=1
#     print("factorial of number is", fac)
# f()

# a="Monika"
# print(a[::-1])


# def febo(n):
#     if n==1:
#         return 0
#     if n==2:
#         return 1
#     return (febo(n-1)+febo(n-2))
# num=int(input("enter no"))
# for i in range(1, num+1):
#     print(febo(i))

# s= "P@#yn26at^&i5ve"
# a=0
# b=0
# c=0
# d=0
# for i in s:
#     if i.isdigit()==True:
#         a+=1
#     elif i.isupper()==True:
#         b+=1
#     elif i.islower()==True:
#         c+=1
#     else:
#         d+=1
# e=b+c
# print("char",e)
# print('digit values:',a)
# print('special charc:',d)

# s = "English = 78 Science = 83 Math = 68 History = 65"
# a=s.split()
# # print(a)
# su=0
# m=[]
# for i in a:
#     if i.isdigit()==True:
#         m.append(int(i))
# print(sum(m))
# print(sum(m)/4)

# a="My name is Sam, Sam live in Mumbai, Sam like it"
# b=a.split()
# print(b)
# d=b[::-1]
# for i in d:
#     print(i,end=" ")

# i=0
# while i<len(b):
#     c=b[-i-1]
#     i+=1
#     print(c,end=" ")


# a="My name is Sam Sam lives in Mumbai, Sam plays cricket"
# b=a.split()
# c=0
# for i in b:
#     if i=="Sam":
#         c+=1
# print("Sam is occurring",c ,"times")


# a=[12,23,44,55,20,33,45,33,20]
# b=[]
# for i in a:
#     if i==20:
#         i=200
#     b.append(i)
# print(b)

# if 20 in a:
#     a[4]=200
# print(a)


# (('c', 11), ('a', 23), ('d', 29), ('b', 37)).
# from operator import itemgetter
# data=(('a', 23), ('b', 37), ('c', 11), ('d',29))
# print(sorted(data,key=itemgetter(1)))


# set1 = {10, 20, 30, 40, 50}
# set2 = {60, 70, 80, 90, 10}

# se1={1,2,3,4,5}
# se2={6,7,8,9,0}
# s3=set1.intersection(set2)
# s4=set1.union(set2)
# a=se1.isdisjoint(se2)
# print(a)
# s=set2.isdisjoint(set1)
# print(s)
# s5=set1.symmetric_difference(set2)
# print(s3)
# print(s4)
# print(s5)


# a=int(input("enter the number1:-"))
# b=int(input("enter the number2:-"))
# c=int(input("enter the number3:-"))
# if (a>b) and (a>c):
#     big=a
# elif (b>a) and (b>c):
#     big=b
# else:
#     big=c
# print("the big number is",big)

# a="My name is Paul I live in Mumbai"
# vowels = "AaEeIiOoUu"
# f=[]
# for i in a:
#     if i in vowels:
#         f.append(i)
# print(len(f))

"""with function"""
# def Check_Vow(string, vowels):
#     final = [i for i in string if i in vowels]
#     print(len(final))
#     print(final)
# # Driver Code
# string = "My name is Paul I live in Mumbai"
# vowels = "AaEeIiOoUu"
# Check_Vow(string, vowels)

# print(5 % 2)
# print(9 % 5)
# print(15%12)
# print(12 % 15)
# print(0 % 7)
# print(7 % 0)

# ch = input("Please Enter Your Own Character : ")
# # v='aAeEIiOoUu'
# if ch in 'aAeEIiOoUu':
#     print("The Given Character ", ch, "is a Vowel")
# else:
#     print("The Given Character ", ch, "is a Consonant")


username=input("enter the name:-")
if username=="Admin": 
    password=int(input("enter the password:-"))
    if password==123:
        print("Welcome Admin")
    else:
        print("invalid username")
else:
    print("fack user")
