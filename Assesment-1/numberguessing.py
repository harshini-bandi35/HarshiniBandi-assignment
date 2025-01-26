'''Number Guessing Game
   - Develop a program where the computer generates a random number between 1 and 100, and the user guesses the number.
   - Provide hints like "Too High" or "Too Low."
   - Use a loop to allow multiple attempts.
'''
import random
t=input("enter the number of times you want to repeat the process: ")
for i in range(int(t)):
    user_input=input("enter a number: ")
    a=random.randint(0,100)
    print(f"the randomly generated integer is: {a}")
    if(abs(int(user_input)-a)<25):
        print("great! your guess is too high")
    else:
        print("ohh no! your guess is too low")
    
