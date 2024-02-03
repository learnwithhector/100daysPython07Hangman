import random
from words import word_list
from art import logo, stages

chosen_word = random.choice(word_list)

print(logo)
print()
print(f"The word is {chosen_word}")  # TODO - delete after testing

lives = 6
guessed_letters = []
display = []
for letter in chosen_word:
    display.append("_")

# print(display)

while "_" in display:
    print(stages[lives])
    print()
    print(f"You have {lives} li{'fe' if lives == 1 else 'ves'} left")
    print()
    print(display)
    print()
    guess = input("Guess a letter: ").casefold()
    print()
    if guess not in chosen_word:
        if guess not in guessed_letters:
            print(f"`{guess}` is not in the word")
            guessed_letters.append(guess)
            lives -= 1
            if lives == 0:
                print(stages[0])
                print(f"Game over! Bad luck! The word was `{chosen_word}`")
                break
        else:
            print(f"You have already guessed `{guess}`")
    else:
        if guess in guessed_letters:
            print(f"You have already guessed `{guess}`")
        else:
            print(f"`{guess}` is in the word")
            guessed_letters.append(guess)
    for index, letter in enumerate(chosen_word):
        if letter == guess:
            display[index] = guess

else:
    print("Well done you guessed it")
