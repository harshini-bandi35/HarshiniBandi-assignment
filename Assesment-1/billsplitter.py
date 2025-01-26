'''. Bill Splitter
   - Create a program to split a bill among a group of people:
     - Input: Total bill amount, number of people, and any tip percentage.
     - Output: Amount each person has to pay.
'''
total_bill_amount=input("enter the total bill: ")
number_of_people=input("enter the total number of people: ")
tip_percentage=input("enter the tip percentage: ")
bill=(int(total_bill_amount))+(int((total_bill_amount))*((int(tip_percentage))/100))
per_person_amount=bill/int(number_of_people)
print(f"The amount each person has to pay is:{per_person_amount}")