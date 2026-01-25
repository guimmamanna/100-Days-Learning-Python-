weight = float(input("Please Enter your weight here in Kg: \n"))
height = float(input("Please Enter your height here in Cm: \n"))
bmi = weight / (height ** 2)
if bmi < 18.5:
    print(f"Your BMI is {bmi} you are Underweight")

elif bmi >= 18.5 and 25:
    print(f"Your BMI is {bmi} you are Normal")

else:
    print(f"Your BMI is {bmi} you are Overweight")
