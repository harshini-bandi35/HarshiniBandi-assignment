'''String Analysis Tool
   - Write a program to analyze a string:
     - Count vowels, consonants, digits, and special characters.
     - Reverse the string and display the result.
'''
str=input("enter the string: ")
vowels=['a','e','i','o','u']
consonents=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
vowels_count=0
consonents_count=0
digits_count=0
special_count=0
for i in str:
    if i.lower() in vowels:
        vowels_count+=1
    elif i.lower() in consonents:
        consonents_count+=1
    elif i.isdigit():
        digits_count+=1
    else:
        special_count+=1
print(f"The total number of vowels are:{vowels_count}")
print(f"The total number of consonents are:{consonents_count}")
print(f"The total number of digits are:{digits_count}")
print(f"The total number of special are:{special_count}")
print("The reversed string is:",str[::-1] )        
