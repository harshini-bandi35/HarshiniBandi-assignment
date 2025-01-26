'''11. Password Strength Checker
   - Develop a program to check the strength of a password:
     - Criteria: At least 8 characters, includes uppercase, lowercase, digits, and special characters.

'''
password=input("enter your password: ")
count1=0
count2=0
count3=0
count4=0
special=['!','@','#','$','%','^','&','*']

if (len(password)>=8):
    for i in password:
        if i.islower():
            count1+=1
        if i.isupper():
            count2+=1
        if i.isdigit():
            count3+=1
        if i in special:
            count4+=1
    if count1>=1 and count2>=1 and count3>=1 and count4>=1:
        print("your password is very strong")
    else:
        print("your password is not strong,please use another password!!")
else:
    print("use a password of length greater than or equal to 8")
        
