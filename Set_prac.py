sample_set = {"Yellow", "Orange", "Black","green"}
sample_list = ["Blue", "green", "Red","Black"]
s=set(sample_list)
# sample_list.pop()
# sample_set.pop()
# print(sample_list)
# print(s)
# sample_set.update(s)
# print(sample_set)

# s3=s.intersection(sample_set)
# s2=s.symmetric_difference(sample_set)
# s4=s.union(sample_set)
# print(s4)
# print(s2)
# print(s3)


d={}
d["name"]="mona"
d["age"]=21
d["place"]="ujjain"
print(d)
k=input("Enter key U want to remove:-")
for i in d:
    if i==k:
        print(d[i])


# if i in d:
#     # d.pop(i)
#     del d[i]
#     print(d)
