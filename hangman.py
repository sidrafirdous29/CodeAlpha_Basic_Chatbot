import random

words = ["python", "apple", "mobile", "coding", "hello"]

secret_word = random.choice(words)
guessed_letters = []
attempts = 6

print("===== HANGMAN GAME =====")
print("Guess the secret word!")
print("You have 6 wrong attempts.")

while attempts > 0:
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Attempts left:", attempts)

    if all(letter in guessed_letters for letter in secret_word):
        print("Congratulations! You Win!")
        break

    guess = input("Guess a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter!")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct guess!")
    else:
        print("Wrong guess!")
        attempts -= 1

else:
    print("\nGame Over!")
    print("The secret word was:", secret_word)
