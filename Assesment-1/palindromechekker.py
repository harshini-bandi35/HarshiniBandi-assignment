'''13. Palindrome Checker
   - Write a program to check if a given string or number is a palindrome.
   - Allow the user to input multiple values using a loop.

'''
t=int(input("enter the number of times you want to give input: "))
for i in range(t):
    user_input=input("enter anything you want: ")
    if user_input==user_input[::-1]:
        print(f"The input you have entered is a palindrome")
    else:
        print(f"sorry! The input you entered is not a palindrome")
