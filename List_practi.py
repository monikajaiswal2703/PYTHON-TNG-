# name1=input("Enter First Name:")
# name2=input("Enter Second Name:")
# name3=input("Enter Third Name:")
# print('"'+name1,name2,name3+'"',sep = "  ")

# Name= input("Enter Name:")
# Age= int(input("Enter Age:"))
# print(Name,Age, sep= '\n')


# a=9
# b=20.4
# c="mona"
# d=True
# print(a,b,c,d, sep= ",")

# a=10
# a=float(a)
# print(a,type(a))


# a=8
# print(oct(a))

# a=24
# print(oct(a))

# n=[76,90,4,65,43,67,20,87,97,56,67]
# if 20 in n:
#     i=n.index(20)
#     print(i)
#     n[i]=200
#     print(n)
# else:
#     print("20 is not present in n")

# a=int(input("enter the number"))
# if a%2==0:
#    print("even number",a)
# else:
#    print("odd number",a)

# a=int(input("enter the number"))
# if a%5==0:
#    print("Divisibl",a)
# else:
#    print("not Divisibl",a)


# a=int(input("enter the number1:-"))
# b=int(input("enter the number2:-"))
# c=int(input("enter the number3:-"))
# if (a>b) and (a>c):
#    big=a
# elif (b>a) and (b>c):
#    big=b
# else:
#    big=c
# print("the big number is",big)

# i=1
# while i<=250:
#    if i%2!=0:
#        print("even",i)
#    i+=1

# i=1
# while i<=25:
#    if i%2==0:
#        print("even",i)
#    i+=1


# "q5"Write a program using while loop to evaluate factorial of a number.
# num=int(input("enter the number"))
# f=1
# for i in range(1,num+1):
#     f=f*i
# print(f)

# age=int(input("enter the age:-"))
# if (age>=18 and age<=60):
#    print("eligible for vote")
# # elif (age>=0 and age<=18):
# else:
#    print("Not eligible for vote")


# a = ["apple","banana",2344,45.687,"apple",12,33,44,56,"monika"]
# a.insert(4,"swati")
# print(a)

# a = ["apple","banana",2344,45.687,"apple",12,33,44,56,"monika"]
# a.append("swati")
# print(a)

# a = ["apple","banana",2344,45.687,"apple",12,33,44,56,"monika"]
# a.extend("swati")
# print(a)

# a = ["apple","banana",2344,45.687,"apple",12,33,44,56,"monika"]
# b=[1,"mona",2,3]
# b.extend(a)
# print(b)

# tup=(11,[22,33],44,55)
# # tup=list(tup)
# tup[1][0]=200
# print(tup)

# a=[1,2,3,4,5,62,7,88]
# a.sort()
# print(a)
# a.append(4)
# print(a)
# a.remove(88)
# print(a)
# a.pop()
# print(a)
# del a[1]
# print(a)

# i = 10
# while i > 1:
#     if i == 5:
#        break
#     # i-=1
#     print(i)
#     i-=1

# for i in range(10,1,-1):
#     if i==5:
#         break
#     print(i)

# a=[12,22,33,30,20,50,55,66]
# b=[]
# for i in a:
#     if i==33:
#         i=200
#     b.append(i)
# print(b)

# String = "morning"
# def data(string):
# 	string = "Good Morning"
# 	print("Inside the Function",string)
# data("string")
# print("Outside the Function",String)

# class Employee:
#     def __init__(self, name, empCode,pay):
#         self.name=name
#         self.empCode=empCode
#         self.pay=pay
# e1 = Employee("Sarah",99,30000.00)
# e2 = Employee("Asrar",100,60000.00)
# # print("Employee Details:")
# # print(" Name:",e1.name,"Code:", e1.empCode,"Pay:", e1.pay)
# # print(" Name:",e2.name,"Code:", e2.empCode,"Pay:", e2.pay)

# class Child(Employee):
#     def __init__(self, name, empCode, pay, salary):
#         super().__init__(name, empCode, pay)
#         self.salary=salary
# obj= Child("Mona",55,678,39000)
# print("Name",obj.name,"e_code",obj.empCode,"pay",obj.pay,"e_salary",obj.salary)

# list=[10,20,30,40]
# list.remove(30)
# print(list)
# del list[1]
# print(list)

# input_str = "Amazon Prime is a great OTT Platform"
# print(input_str.swapcase())
		# "aMAZON pRIME IS A GREAT ott pLATFORM."

# a="  1,5,6,4,3,7,mona  m"  
# print(a.strip())

# a="  1,5,6,4,3,7,mona  m"  
# print(a.split(','))

# a=["  1,5,6,4,3,7,mona  m"]  
# print(''.join(a))

# import random
# a=[1,5,6,4,3,7,"mona"] 
# print(random.choice(a))
# print ("Reshuffled list : ", a)

# a=[1,5,6,4,3,7,"mona"] 
# print(random.choices(a))
# print ("Reshuffled list : ", a)

# a=[1,5,6,4,3,7,"mona"] 
# print(random.shuffle(a))
# print ("Reshuffled list : ", a)

# a=[1,2,3,1,4,"mona",2,3,"mona"]
# "1 st way"
# d=[]
# for i in range (len(a)):
#     for j in range(i+1, len(a)):
#         if a[i]==a[j] and a[i] not in d:
#             d.append(a[i])
# print(d) 

# "2 nd way"
# a=[1,2,3,1,4,"mona",2,3,"mona"]
# d=[]
# for i in a:
#     if a.count(i)>1 and i not in d:
#         d.append(i)
# print(d)

# a=[1,2,3,4,5,6,8,5,4]
# evens= list(filter(lambda n: n%2==0, a))
# mapped=list(map(lambda x:x*3,evens))
# from functools import reduce
# sum=reduce(lambda a,b:a+b, mapped)
# print(sum)
# print(mapped)
# print(evens)


# a=list(map(int,input().split()))
# b=max(a)
# c=a.index(b)
# print("{} is the max no. of list at index {}".format(b,c))

# s="1234abcd"
# def fun(s):
# 	return s[::-1]
# 	# return "".join(reversed(s))
# print(fun(s))

# itm=[]
# for i in range(100,301):
# 	num=str(i)
# 	f=int(num[0])
# 	s=int(num[1])
# 	t=int(num[2])
# 	if (f%2==0) and (s%2==0) and (t%2==0):
# 		itm.append(num)
# print(",".join(itm))




# def fMax(a):
# 	lis=[]
# 	li1=[]
# 	for i in a:
# 		lis.append(max(i))
# 		li1.append(min(i))
# 		# return lis
# 	print(lis,sum(lis))
# 	print(li1,sum(li1))
# a = [[10, 13, 454, 66, 44], [10, 8, 7, 23],[12,3,4,2]]
# fMax(a)
# for i in lis
# # lis = []
# # find max in list
# for p in a:
#     # lis.append(max(p))
# 	print(p)
# # Printing max
# print(lis)


# a=input()
# if type(a)==int:
# 	print(type(a))
# elif type(a)==str:
# 	print(type(a))
# else:
# 	print(type(a))

#"Accept a string with "#" as a separator. Use the spilt method to display the strings in a list"
# a="monika # jaiswal # is # my # name"
# b=a.split("#")
# print(b)

#"q 9 Accept a number from the user and test whether it is zero,
# positive or negative number. Display a message accordingly"
# a=int(input())
# if a>0:
# 	print("positive")
# elif a==0:
# 	print("Zero")
# else:
# 	print("negative")

# "q10 Write a program to display and find the sum of a list of numbers"
# a=[1,2,3,4,5,6,7]
# s=0
# for i in a:
# 	s+=i
# print(s)


for i in range(10,5,-1):
	if i==5:
		break
	print(i)