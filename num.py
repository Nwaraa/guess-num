import random

number = random.randint(1, 100)
guess = -1

while guess != number:
  guess = int(input("Guess a number from 1-100: "))

  if guess >= 1 and guess <= 100:
    if guess > number:
      print("Guess lower!")
    elif guess < number:
      print("Guess higher!")
