# def abc(name,age):
#     print("name is",name,"\n age is",age)
# abc("mona",21)

# def arb(*n):
#     for i in n:
#         print(i)
# arb("mona","shivi",12,12.9,True)


# def calcu(n,n1,s):
#     if s=="+" or s=="-":
#         return(n+n1 , n-n1)
# n=int(input("enter the number1:-"))
# n1=int(input("enter the number2:-"))
# s=input("enter the symbol")
# print(calcu(n,n1,s))

# def showEmployee(E_name,salary=5000):
#     print("employee name is",E_name)
#     print("salary is",salary)
# showEmployee("swapnil",90000)    

# def outer(a,b):
#     x=0
#     def inner():
#         nonlocal x
#         x=a+b
#     inner()
#     x+=5
#     return x
# print(outer(4,3))

# def s1(n):
#     if n==0:
#         return n
#     return n+s1(n-1)
# n=10
# print(s1(n))

# # Exercise 7: Assign a different name to function and call it through the new name.
# def a():
#     print(2+5)
# b=a()
# print(type(a))


# even=lambda a:[i for i in range(1,a) if i%2==0] 
# print(even(20))
 
even_nos = list(filter(lambda x: (x % 2 == 0)))
print("Even numbers in the list: ", even_nos(4,46))
