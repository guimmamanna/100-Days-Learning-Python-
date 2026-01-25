import random
word_list = ["aardvark", "baboon", "camel"]

# Generate a random word
random_guess = random.choice(word_list)
print(random_guess)

# User guess a letter

guess = input("Guess any letter of your choice: ")
print(guess)

# Generate blanks
blanks = ["_"] * len(random_guess)

# Replace blank with letters
for index, letter in enumerate(random_guess):
    if letter == guess:
        blanks[index] = letter
        replace = ("".join(blanks))
# Are all blanks filled?

# Are all blanks filled?
while "".join(blanks) != random_guess:
    guess = input("Guess a letter: ")
    for i, ch in enumerate(random_guess):
        if ch == guess:
            blanks[i] = ch
    print("".join(blanks))
