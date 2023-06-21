import random
import time 

print("Hi welcome to the guessing game, please guess the number between  1 and 100.")
time.sleep(3)
print("Picking a number...")
time.sleep(2)
guess = int(input("What is your guess?: "))
correct_number = random.randint(1, 100)
guess_count = 1

while guess != correct_number: #while this condition is true - the guessed number is not 5 it will print below print statement
    guess_count += 1 #add one to each guess

    if guess < correct_number:
        guess = int(input(f"Wrong answer. You need to guess higher. What is your guess?: "))
    else:
        guess = int(input(f"Wrong answer. You need to guess lower. What is your guess?: "))

print(f"Congrats You got the right answer! :-) The right answer was {correct_number} and it took you {guess_count} guesses.") #this prints once user guesses the correct number 