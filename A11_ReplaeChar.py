def swap (user_input, str1, str2):
    result = ''
    if user_input != None:
        result = user_input.replace(str1, '*').replace(str2, str1).replace('*', str2)
        return result
    return 'Null'
user_input = input()
str1, str2 = map(str,input().split())
print(swap(user_input, str1, str2))

# Input:
# Str: apples
# ch1:a
# ch2:p
# Output:
# paales