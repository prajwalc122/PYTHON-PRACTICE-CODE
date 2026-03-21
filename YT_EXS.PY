# user sets the secret number
number = int(input("Enter a secret number: "))

print("\n" * 20)  # hide the number (simple trick)

guess = 0
attempts = 0

while guess != number:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess > number:
        print("Too High!")

    elif guess < number:
        print("Too Low!")

    else:
        print("Correct! You guessed it!")
        print("Attempts:", attempts)