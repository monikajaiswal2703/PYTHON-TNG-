def countExponents(i):
    count = 0
    while i%2 == 0 and i != 0:
        count+=1
        i = i//2
    return count
def maxExponents(a, b):
    maximum, number = 0, a
    for i in range(a,b):
        temp = countExponents(i)
        if temp>maximum:
            maximum, number = temp, i
    return number
a, b = map(int,input().split())
print(maxExponents(a, b))

# Example

# Input:
# 7
# 12
# Output:
# 8
# Explanation:

# Exponents of 2 in:

# 7-0

# 8-3

# 9-0

# 10-1

# 11-0

# 12-2

# Hence maximum exponent if two is of 8