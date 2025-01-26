'''. Bank Loan Eligibility
   - Develop a program to check loan eligibility:
     - Input: Salary, age, and credit score.
     - Output: Loan approval or rejection with reasons.
'''
def user_input():
    salary=input("enter the salary of the user: ")
    age=input("enter the age of the user: ")
    credit_score=input("enter the credit score of the user: ")
    return (salary, age, credit_score)
def compute_loan(salary, age, credit_score):
    if int(salary)>15000 and int(age)>18 and int(credit_score)>60:
        output="Your loan is sanctioned"
    elif(int(salary)<15000):
        output="your salary should be more than 15000"
    elif(int(age)<18):
        output= "your age should be greater than 18"
    elif (int(credit_score)<60):
        output= "your credit score should be greater than 60"
    elif(int(salary)<15000 and int(age)<18):
        output= "both your salary and age ara not upto the limit"
    elif(int(salary)<15000 and int(credit_score)<60):
        output= "both your salary and credit_score ara not upto the limit"
    elif(int(age)<18 and int(credit_score)<60):
        output= "both your age and credit_score ara not upto the limit"
    else:
        output= "you are loan is rejected because of all your inputs"
    return output
def display(output):
    print(f"your status is :{output}")
def main():
    (salary,age,credit_score)=user_input()
    output=compute_loan(salary,age,credit_score)
    display(output)
main()

