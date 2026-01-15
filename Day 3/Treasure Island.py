print("Welcome to Treasure Island \n")
print("Your Mission is to find the treasure \n")

direction = input("Where do you want to go: left or right \n")
if direction == "right":
    print("You have fallen into a hole. Game Over")
if direction == "left":
    choose = input("Swim or Wait? \n")
    if choose == "swim":
        print(" You have been attacked trout. Game Over")
    elif choose == "wait":
        door = input("Choose a door! Red, Blue or Yellow \n")
        if door == "red":
            print("You have been burned by fire. Game Over")
        if door == "blue":
            print("You have been Eaten by beasts. Game Over")
        if door == "yellow":
            print("You Win")
        else:
            print("Game over")
else:
    print("input a correct designation")
