print("Welcome to Pizza hut!")

small_pizza = 15
medium_pizza = 20
large_pizza = 25
size = input("What Size of pizza do you want? S, M or L: ")
# Small Pizza

if size == "S":
    print(f"The cost of a Medium Pizza is £ {small_pizza} \n")
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    extra_cheese = input("Do you want extra cheese? Y or N: ")
    if pepperoni == "Y" and extra_cheese == "Y":
        bill_1 = small_pizza + 2 + 1
        print(f" The Total bill is £ {bill_1}")
    if pepperoni == "Y" and extra_cheese == "N":
        bill_2 = small_pizza + 2
        print(f" The Total bill is £ {bill_2}")
    if pepperoni == "N" and extra_cheese == "Y":
        bill_3 = small_pizza + 1
        print(f" The Total bill is £ {bill_3}")
    if pepperoni == "N" and extra_cheese == "N":
        print(f" The Total bill is £ {small_pizza}")

# Medium Pizza

if size == "M":
    print(f"The cost of a Medium Pizza is £ {medium_pizza} \n")
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    extra_cheese = input("Do you want extra cheese? Y or N: ")
    if pepperoni == "Y" and extra_cheese == "Y":
        bill_1 = medium_pizza + 3 + 1
        print(f" The Total bill is £ {bill_1}")
    if pepperoni == "Y" and extra_cheese == "N":
        bill_2 = medium_pizza + 3
        print(f" The Total bill is £ {bill_2}")
    if pepperoni == "N" and extra_cheese == "Y":
        bill_3 = medium_pizza + 1
        print(f" The Total bill is £ {bill_3}")
    if pepperoni == "N" and extra_cheese == "N":
        print(f" The Total bill is £ {medium_pizza}")

# Large Pizza

if size == "L":
    print(f"The cost of a Medium Pizza is £ {large_pizza} \n")
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    extra_cheese = input("Do you want extra cheese? Y or N: ")
    if pepperoni == "Y" and extra_cheese == "Y":
        bill_1 = large_pizza + 3 + 1
        print(f" The Total bill is £ {bill_1}")
    if pepperoni == "Y" and extra_cheese == "N":
        bill_2 = large_pizza + 3
        print(f" The Total bill is £ {bill_2}")
    if pepperoni == "N" and extra_cheese == "Y":
        bill_3 = large_pizza + 1
        print(f" The Total bill is £ {bill_3}")
    if pepperoni == "N" and extra_cheese == "N":
        print(f" The Total bill is £ {small_pizza}")

else:
    print(f" Choose Correct Options as Indicated on the Board")
