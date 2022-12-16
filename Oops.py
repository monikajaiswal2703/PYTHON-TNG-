# class parent_class:  
#     def Summation(self,num1,num2):  
#         return num1+num2;  
# class child_class(parent_class):  #inheriting parent_class
#     def Average(self,num1,num2): 
#         return num1//num2;  
# fm=child_class() 
# print(fm.Average(100,20))
# print(fm.Summation(78,10)) #accessing parent_class method with object of child_class

# class Square:
#     def Area(self,side): #definiting method with 1 argument
#         return side*side
# class Rectangle(Square):
#     def Area(self,length,bredth): #overriding method with 2 arguments
#         return length*bredth
# class Circle(Square):
#     def Area(self,radius):
#         return 2*3.14*radius*radius #overriding method with 1 argument
# sqr = Square()
# rct = Rectangle()
# crc = Circle()
# print(sqr.Area(12))
# print(rct.Area(12,10))
# print(crc.Area(6))

# Q1. Write a Python program to create a Vehicle class with max_speed and mileage instance.
# "1st method"
# class Vehicle():
#     max_speed=80
#     mileage=50
# #print(Vehicle.max_speed)
# "instance"
# a=Vehicle()
# b=Vehicle()
# print(a.mileage,b.max_speed)

#2 nd way
# class Vehicle():
#  def __init__(self,max_speed,mileage):
#         self.max_speed=max_speed
#         self.mileage=mileage
        
# hero=Vehicle(140,60)
# honda=Vehicle(120,72)

# print(hero.max_speed,hero.mileage)
# print(honda.max_speed,honda.mileage)
# class Bike(Vehicle):
#     def __init__(self, max_speed, mileage, Price, model):
#         super().__init__(max_speed, mileage)
#         self.Price=Price
#         self.model=model
# h=Bike(120,90,45000,2018)
# # print(h.max_speed,h.mileage,h.Price,h.model)

# class Bus(Bike):#child class
#    def __init__(self, max_speed, mileage, Price, model,capacity,build_year):
#        super().__init__(max_speed, mileage, Price, model)
#        self.capacity=capacity
#        self.build_year=build_year
# s1=Bus(120,90,45000,2018,"200kg",2014)
# print(s1.max_speed,s1.mileage,s1.Price,s1.model,s1.capacity,s1.build_year)


# class Student():
#     school_name= "vikram"
#     school_name1="Education"
#     def __init__(self,name,age,Class):#instance variables
#         self.name = name # initialise the instance variable
#         self.age = age
#         self.Class = Class
# a=Student("aashu",12,"6th")
# b=Student("dipu",8,"4th")
# print(a.name,a.age,a.Class,a.school_name1) 
# print(b.name,b.age,b.Class, b.school_name)    


# class Grand_f: #base class/ Parent class
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# class Father(Grand_f):#child class / derived class
#     def __init__(self,name,age,gender,grade):
#         Grand_f.__init__(self,name,age)#inheriting
#         self.gender = gender
#         self.grade = grade
# t1 = Father("swam",33,"male",14)
# print(t1.name,t1.age,t1.gender,t1.grade)

# class Student(Father):
#     def __init__(self,name,age,gender,school_name,fees,class_name):
#         Grand_f.__init__(self,name,age)
#         self.gender = gender
#         self.school_name = school_name
#         self.fees = fees
#         self.class_name=class_name
# s1 = Student("viv",12,"male","ABC",20000,"10th")
# print(s1.name,s1.age,s1.gender,s1.school_name,s1.fees,s1.class_name)
# class Friend(Student):
#     def __init__(self,name,age,gender,fees,fav_place,birth_year):
#         Father.__init__(self,name,age,gender,fees)
#         Grand_f.__init__(self,name,age)
#         self.fav_place=fav_place
#         self.birth_year=birth_year
#         self.fees=fees
# a1 = Friend("shivi",22,"female","ujjain",20000,2000)
# print(a1.name,a1.age,a1.gender,a1.fav_place,a1.fees,a1.birth_year)
    

# class Student():
#      def __init__(self,name,student_ID,marks):#instance variables
#         self.name = name # initialise the instance variable
#         self.student_ID = student_ID
#         self.marks = marks
# a=Student("mona","m123",80)
# print(a.name)
# print(a.name,a.marks,a.student_ID)

# Q17. Create a simple calculator using functions.
# class Calcu():
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self):
#         return self.a+self.b
#     def sub(self):
#         return self.a-self.b
#     def multy(self):
#         return self.a*self.b
#     def divi(self):
#         return self.a/self.b
#     def floor_divi(self):
#         return self.a//self.b
# a1=Calcu(4,13)
# print(a1.add())
# print(a1.multy())
# print(a1.sub())
# print(a1.divi())
# print(a1.floor_divi())
