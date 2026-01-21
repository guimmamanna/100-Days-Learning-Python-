import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

length = len(chosen_word)
placeholder = ""

for position in range(length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []
lives = 6

while not game_over:
    guess_letter = input("Guess a Letter: ").lower()

    if guess_letter in correct_letters:
        print(f"You have already guessed {guess_letter}")
    display = ""

    for letter in chosen_word:
        if letter == guess_letter:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    if guess_letter not in chosen_word:
        lives -= 1
        print(f"You have already guessed {guess_letter}")
        if lives == 0:
            game_over = True
            print(f"IT WAS {chosen_word}")
    print(display)

    if "_" not in display:
        game_over = True
        print("You Win")
