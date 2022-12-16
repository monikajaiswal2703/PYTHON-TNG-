# txt = "Hello, welcome to my world."
# x = txt.endswith(".")
# print(x)

# txt = "Hello, welcome to my world."
# x = txt.endswith("my world.", 5, 11)
# print(x)

# "2nd"
# txt = "H\te\tl\tl\to"

# print(txt)
# print(txt.expandtabs())
# print(txt.expandtabs(2))
# print(txt.expandtabs(4))
# print(txt.expandtabs(10))

"3 format"
# txt = "For only {price:.1f} dollars!"
# print(txt.format(price = 49))

#named indexes:
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
#numbered indexes:
txt2 = "My name is {0}, I'm {1}".format("John",36)
#empty placeholders:
txt3 = "My name is {}, I'm {}".format("John",36)
print(txt1)
print(txt2)
print(txt3)
