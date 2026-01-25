import random
user_input = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
print(user_input)
random_choice = random.randint(0, 2)
print(random_choice)
if random_choice == user_input:
    print("This is a Draw")
elif random_choice == 0 and user_input == 1:
    print("You Win")
elif random_choice == 1 and user_input == 2:
    print("You Win")
elif random_choice == 2 and user_input == 0:
    print("You Win")
else:
    print("You lose")
