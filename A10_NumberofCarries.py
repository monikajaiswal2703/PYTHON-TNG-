def NumberOfCarries(n1,n2):
    count=0
    carry = 0
    if len(n1) <= len(n2):
        l= len(n1)-1
    else:
        l = len(n2)-1
    for i in range(l+1):
        temp = int(n1[l-i])+int(n2[l-i])+carry
        if len(str(temp))>1:
            count+=1
            carry = 1
        else:
            carry = 0
    return count+carry
n1=input("Enter 1 st no.:-")
n2=input("Enter 2 nd no:-")
print(NumberOfCarries(n1,n2))

# Input
# Num 1: 451
# Num 2: 349
# Output
# 2
# Explanation:

# Adding ‘num 1’ and ‘num 2’ right-to-left results in 2 carries since ( 1+9) is 10. 1 is
#  carried and (5+4=1) is 10, again 1 is carried. Hence 2 is returned.