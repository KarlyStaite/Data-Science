import random
ran = random.randint(1,10)
name = input("What is your name? ")
guess = input(name + " guess the number between 1 and 10 I am thinking of? ")

if ran == int(guess):
    print(name,"you chose wisely")
else:
    print(name,"you chose poorly. I was thinking of",ran)