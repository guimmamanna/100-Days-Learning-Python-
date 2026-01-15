# BMI Calculator
# The body mass index (BMI) is a measure used in medicine to see if someone is underweight or overweight. This is the formula used to calculate it:
# bmi is equal to the person's weight divided by the person's height squared.

height = input("What is your height? \n")
weight = input("What is your weight? \n")

x = float(height)
y = float(weight)
z = x**2

bmi = y/z

t = round(bmi, 2)


print(f"Your BMI is = {t}")
