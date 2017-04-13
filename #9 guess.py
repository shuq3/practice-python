# use while loop to control a game
import random

right = random.randint(0, 9)
count = 0;
mes = input("Type 'quit' to quit the game, other to start: ")
while(mes != 'quit'):
    guess = int(input("Guess a num: "))
    if guess < right:
        print("Your guess is lower than the right one.")
    elif guess > right:
        print("Your guess is higher than the right one.")
    else:
        count += 1;
        print("You are right")
        right = random.randint(0, 9)
        mes = input("Type 'quit' to quit the game, other to start: ")

print (count)
