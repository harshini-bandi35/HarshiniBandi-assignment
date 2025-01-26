'''14. Factorial Calculator
   - Create a program to calculate the factorial of a number using a loop.
   - Include error handling for negative numbers.

'''
num=int(input("enter a number to find factorial: "))
factorial=1
if num<0:
    print("please give a positive number to find factorial")
elif num==0:
    print("the factorial of zeros is :1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print(f"The factorial of the number is {factorial}")