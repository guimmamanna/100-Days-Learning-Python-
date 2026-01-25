print("Welcome to the Rollercoaster")
height = int(input("What is your height in cm:"))
if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("What is your age: "))
    if age < 12:
        print(f"You have to pay £{5}")
        photo = input(
            "Do you want to have a photo taken? Type y for Yes and n for No \n")
        if photo == "y":
            print(f"Your final bill is £{5+3}")
        elif photo == "n":
            print(f"Your final bill is £{5}")
    elif age > 18:
        print(f"You have to pay £{12}")
        photo = input(
            "Do you want to have a photo taken? Type y for Yes and n for No \n")
        if photo == "y":
            print(f"Your final bill is £{12+3}")
        elif photo == "n":
            print(f"Your final bill is £{12}")
    elif age >= 12 and 18:
        print(f"You have to pay ${7}")
        photo = input(
            "Do you want to have a photo taken? Type y for Yes and n for No \n")
        if photo == "y":
            print(f"Your final bill is £{7+3}")
        elif photo == "n":
            print(f"Your final bill is £{7}")

    else:
        print(f"You have to pay ${12}")
        photo = input(
            "Do you want to have a photo taken? Type y for Yes and n for No \n")
        if photo == "y":
            print(f"Your final bill is £{12+3}")
        elif photo == "n":
            print(f"Your final bill is £{12}")

else:
    print("Sorry you have to grow taller before you can ride.")
