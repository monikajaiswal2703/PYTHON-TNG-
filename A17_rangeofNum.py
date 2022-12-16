n=int(input("Enter 1st num:-"))
ln=int(input("Enter last number:-"))
for i in range(n+1,ln,11):
    print(i,end=", ")

# Palindrome Number Checking

# first_number = int(input())
# second_number = int(input())

# for i in range(first_number, second_number+1):
#     reverse = 0
#     temp = i
#     while temp != 0:
#         remainder = temp % 10
#         reverse = (reverse * 10)+remainder
#         temp = temp // 10
#         if i == reverse:
#             print(reverse, end=" ")