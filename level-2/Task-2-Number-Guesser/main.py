import random
print("===== Number Guesser =====")
# User enters the range
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
# Generate random number
secret_number = random.randint(start, end)
print(f"\nGuess the number between {start} and {end}")

while True:
    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Too Low! Try Again.")

    elif guess > secret_number:
        print("Too High! Try Again.")

    else:
        print("Congratulations! You guessed the correct number.")
        break