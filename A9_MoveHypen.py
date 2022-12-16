inp = input()
count = 0
final = ""
for i in inp:
    if i == '-':
        count+=1
    else:
        final+=i
print("-"*count,final)

# Input:
# str.Move-Hyphens-to-Front
# Output:
# —MoveHyphenstoFront