# t1 =("a","b","c","a","f","d","a")
# print(t1.count("a"))

# Q12. Write a program to know whether a sub string is there in the main string or not.
# s=input("enter string:-")
# sub_string=input("enter word:-")
# if (s.find(sub_string)==-1):
#     print("Substring not found in string")
# else:
#     print("Substring in string")


# s=input("enter string:-")
# sub_string=input("enter word:-")
# r=0
# for i in range(len(s)):
#     if s[i]==sub_string:
#         r=i+1
# if r==0:
#     print("No available this char.")
# else:
#     print(sub_string,"is present at",(r))
    # print("char. {} is present at {}".format(sub_string,str(r)))


# a=(12,2,3,4,2,4,5,5,66,76,33,5)
# c=0
# u=int(input("enter the number:-"))
# for i in a:
#     if i==u:
#         c+=1
# print(c)

# num1=int(input("enter the number"))
# num2=int(input("enter the number"))
# sign=input("enter the sign")
# if sign=="+" or sign=="-"or sign=="*"or sign=="/":
#     print(num1+num2, num1-num2, num1*num2, num1/num2)

# # "local variable"
# def f():
#     #local 
#     s="I love my mom"
#     print(s)
# f()

# # "Global variable"
# def f():
#     #local 
#         print("inside of fun.",s)
# s="I love my mom"
# f()
# print(s)

# s1 = "Ault"
# s2 = "Kelly"
# s3=s1+s2
# s4=s3[0:2]
# print(s4)
# s5=s3[4::]
# print(s5)
# s6=s3[2:4]
# print(s6)
# print(s4+s5+s6)



# import numpy  
# #method 1  
# array_1 = numpy.array([])  
# print(array_1)  
# #method 2  
# array_2 = numpy.empty(shape=(3,3))  
# print(array_2)  

# tuple_ = (5, 2, 24, 3, 1, 6, 7)  
# sorted_ = tuple(sorted(tuple_, reverse=True))  
# sorted_ = tuple(sorted(tuple_, reverse=False))  
# print('Sorted Tuple :', sorted_)  
# print(type(sorted_))  

tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d',29))
#o/p (('c',11), ('a', 23),('d',29), ('b', 37))
def sort(t):
    for i in range(len(t)):
        for j in range(len(t)-1):
            if (t[j][1]> t[j+1][1]):
                temp=t[j]
                t[j]=t[j+1]
                t[j+1]=temp
    return t
l=list(tuple1)
print(sort(l))

# roll = [('Arshia', 26), ('Itika', 53), ('Peter', 82), ('Parker', 74), ('MJ', 45)]   
# first = 0   
# last = len(roll)   
# for k in range(0, last):   
#     for l in range(0, last-k-1):   
#         if (roll[l][first] > roll[l + 1][first]):   
#             new_item = roll[l]   
#             roll[l]= roll[l + 1]   
#             roll[l + 1]= new_item   
# print(roll)  