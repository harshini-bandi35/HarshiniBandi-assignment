'''Odd and Even Separator
   - Write a program that takes a list of numbers as input and separates them into odd and even lists.'''
list=list(map(int,input().split(' ')))
even=[]
odd=[]
for i in range(len(list)):
    if list[i]%2==0:
        even.append(list[i])
    else:
        odd.append(list[i])
print(f"The even list is:{even}")
print(f"The odd list is:{odd}")

