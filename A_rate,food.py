def calculate(r,unit,arr,n):
    if n==0:
        return -1
    totalFoodRequired=r*unit
    foodTillNow=0
    house=0
    for house in range(n):
        foodTillNow+=arr[house]
        if foodTillNow >= totalFoodRequired:
            break
    if totalFoodRequired > foodTillNow:
        return 0
    return house+1
r = int(input("enter no of rate"))
unit = int(input("enter unit"))
n = int(input("enter size of array"))
arr = list(map(int,input("enter value of array").split()))
print(calculate(r,unit,arr,n))