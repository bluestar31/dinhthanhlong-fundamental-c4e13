from random import randint

#1. Pick a random number (1 - 100)
gmn = randint(1,100)
count = 1

while count <= 8:
    guess = int(input("Guess my number (1 - 100)? "))
    if guess == gmn and count <= 8:
        print("Bingo")
        break
    elif guess < gmn and count < 8:
        print("Too small")
        print("You have", 8 - count, "turns left")
    elif guess > gmn and count < 8:
        print("Too large")
        print("You have", 8 - count, "turns left")
    count += 1
    if count > 8:
        print("You lose")
