# Q26. Write a program to :
# - Read the data from an existing file
# - Append data to the file
# - Display the data with newly appended data.
# "creat a file"
# f = open("abc1.txt",'w')
# a=f.write("i love mahakal\n he is live in ujjain")
# f.close()

# # "Read the data from an existing file"
# d=open("abc1.txt","r")
# print(d.read())

# # # " Append data to the file"
# f = open("abc1.txt",'a')
# f.write("\nHi i am the newly added line")
# f.close()

# # "Display the data with newly appended data"
d=open("abc1.txt","r")
# print(d.readlines())
# d.seek(0)
# print(d.read())
d.seek(1)
print(d.readline())
    
       
