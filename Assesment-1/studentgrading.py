'''4. Student Grading System
   - Write a program to calculate and display student grades.
     - Input: Student's name and marks for 5 subjects.
     - Output: Total marks, percentage, grade (A/B/C/Fail based on percentage).

'''
def student_input():
    maths=input("enter maths marks: ")
    english=input("enter english marks: ")
    social=input("enter social marks: ")
    science=input("enter science marks: ")
    hindi=input("enter hindi marks: ")
    return (maths,english,social,science,hindi)
def compute_total(maths,english,social,science,hindi):
    total_marks=int(maths)+int(english)+int(social)+int(science)+int(hindi)
    return total_marks
def compute_percentage(maths,english,social,science,hindi):
    total_marks=500
    student_percentage=((int(maths)+int(english)+int(social)+int(science)+int(hindi))/total_marks)*100
    return student_percentage
def compute_grade(student_percentage):
    if(student_percentage>90):
        student_grade="A"
    elif(student_percentage>75):
        student_grade="B"
    elif(student_percentage>50):
        student_grade="C"
    else:
        student_grade="FAIL"
    return student_grade 
def display(total_marks,student_percentage,student_grade):
    print(f"The total marks of the student is {total_marks}")
    print(f"The total percentage of the student is {student_percentage}")
    print(f"The total grade is {student_grade}")
def main():
    (maths,english,social,science,hindi)=student_input()
    total_marks=compute_total(maths,english,social,science,hindi)
    student_percentage=compute_percentage(maths,english,social,science,hindi)
    student_grade=compute_grade(student_percentage)
    display(total_marks,student_percentage,student_grade)
main()