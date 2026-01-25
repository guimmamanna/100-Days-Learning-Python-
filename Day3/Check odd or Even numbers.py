print("Check odd or even numbers")

number = int(input("Enter any number: \n"))
modulus = number % 2

if modulus == 0:
    print("This is an Even number")
else:
    print("This is an Odd number")
