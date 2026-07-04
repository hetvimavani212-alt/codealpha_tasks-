import random

# List of programming languages (each has exactly 6 letters)
words = ["python", "golang", "kotlin", "java", "pascal"]

# Randomly select a word
secret_word = random.choice(words)

# Create display with underscores
display = ["_"] * len(secret_word)

# Variables
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

print("=" * 40)
print("         WELCOME TO HANGMAN")
print("=" * 40)

# Main game loop
while incorrect_guesses < max_attempts and "_" in display:

    print("\nWord: ", " ".join(display))
    print("Guessed Letters:", " ".join(guessed_letters) if guessed_letters else "None")
    print("Remaining Attempts:", max_attempts - incorrect_guesses)

    guess = input("Enter a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter only one alphabet letter.")
        continue

    # Already guessed
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Correct guess
    if guess in secret_word:
        print("✅ Correct Guess!")

        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display[i] = guess

    # Wrong guess
    else:
        incorrect_guesses += 1
        print("❌ Wrong Guess!")

print("\n" + "=" * 40)

# Final Result
if "_" not in display:
    print("🎉 Congratulations! You guessed the word.")
    print("The programming language was:", secret_word)
else:
    print("💀 Game Over!")
    print("You used all 6 incorrect guesses.")
    print("The correct programming language was:", secret_word)

print("=" * 40)