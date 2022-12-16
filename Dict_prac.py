Dict1={"name": "Plato", "country": "Ancient Greece", "born": -427, "teacher": "Socrates", "student": "Aristotle"}
Dict1["born"]=234
Dict1["worsk"] ="[“Apology”,”Phaedo”,”Republic”,”Symposium”]"
# print(Dict1)

Dict2={"name":"mona","son's height":23,"age":22,"teacher": "Socrates", "student": "Aristotle"}
# Dict2["son's height"] -= 2
# Dict2["son's height"] += 2
Dict2["son's height"] *= 2
# print(Dict2)
# print(Dict2.keys())
# print(Dict2.values())
# print(Dict2.get('name'))
# print(Dict2.pop("age"))
# print(Dict2.items())
# print(Dict2.popitem())
# Dict2.update(Dict1)
# print(Dict2)
# del Dict2
# print(Dict2)
print(Dict2.clear())
l = []
for i in Dict2.items():
    l.append(i)
print(l)
