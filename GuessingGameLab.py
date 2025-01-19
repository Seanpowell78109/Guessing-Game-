import random

randomNumber = random.randrange(1, 100)

numberOfGuesses = 1

guess = int(input("Guess a number between 1 to 100: "))

while guess != randomNumber:
    numberOfGuesses += 1 #We increment the numberOfGuesses by 1 each time the loop runs
    if guess > randomNumber: #If the guess is larger than the random number
        print(guess, "is too high.")
        guess = int(input("Guess a lower number: "))
    elif guess < randomNumber: #If the guess is lesser than the random number
        print(guess, "is too low.")
        guess = int(input("Guess a higher number: "))
    else: #If the guess is the same (since we've checked both ranges already)
        print("You got it! ")

print("You guessed correctly", numberOfGuesses, "guesses!")
