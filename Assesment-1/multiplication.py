'''. Multiplication Table Generator
   - Create a program to generate a multiplication table for any number provided by the user.
   - Allow the user to specify the range of the table.
'''
number=int(input("enter the number you want to find the table: "))
range_number=int(input("enter the range till which you want to find: "))
for i in range(1,range_number+1):
    print(f"{number}*{i}","=",number*i)