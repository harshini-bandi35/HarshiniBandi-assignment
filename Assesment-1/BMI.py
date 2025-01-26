'''. BMI Calculator
   - Develop a program to calculate BMI:
     - Input: Weight (kg) and height (m).
     - Output: BMI value and corresponding category (Underweight, Normal, Overweight, Obese).
'''
weight=input("enter your weight in kilograms: ")
height=input("enter your height in metres: ")
Body_mass_index=float(weight)/(float(height)**2)
print(f"your Body mass index is: {Body_mass_index}")
if Body_mass_index<30:
    print("Your are underweight..eat more food")
elif Body_mass_index>30 and Body_mass_index<45:
    print("Good,Your are normal")
elif Body_mass_index>45 and Body_mass_index<55:
    print("you are over weight..reduce your weight")
else:
    print("You are obese, please take care of your fat")