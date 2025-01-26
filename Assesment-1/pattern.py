'''Pattern Generator
   - Create a program that generates the following pattern based on user input `n`:
     *
     **
     ***
     ****
'''
n=int(input("enter the number of lines you want your pattern to be"))
for i in range(1,n+1):
    print(i*"*")
