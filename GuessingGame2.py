import random

def play_game():
  """Plays a number guessing game."""
  randomNumber = random.randrange(1, 100)
  numberOfGuesses = 1
  guess = int(input("Guess a number between 1 to 100: "))

  while guess != randomNumber:
      numberOfGuesses += 1
      if guess > randomNumber:
          print(guess, "is too high.")
          guess = int(input("Guess a lower number: "))
      elif guess < randomNumber:
          print(guess, "is too low.")
          guess = int(input("Guess a higher number: "))

  print("You got it! ")
  print("You guessed correctly in", numberOfGuesses, "guesses!")

while True:
  play_game()
  if input("Play again? (y/n): ").lower() != 'y':
      break
