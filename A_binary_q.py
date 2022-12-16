# def OperationsBinaryString(str):
#     a=int(str[0])
#     i=1
#     while i<len(str):
#         if str[i]=='A':
#             a&=int(str[i+1])
#         elif str[i]=='B':
#             a|=int(str[i+1])
#         else:
#             a^=int(str[i+1])
#         i+=2
#     return a
# str=input()
# print(OperationsBinaryString(str))

s=input()
a=int(s[0])
i=1
while i<len(s):
    if s[i]=='A':
        a&=int(s[i+1])
    elif s[i]=='B':
        a|=int(s[i+1])
    else:
        a^=int(s[i+1])
    i+=2
print(a) 