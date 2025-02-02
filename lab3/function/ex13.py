import random
number = random.randint(1,20)


print("Hello, What is your name?")
name = str(input())


print(f"Well, {name}, I am thinking of a number between 1 and 20.
Take a guess.")
while True:
    guess = int(input("guess the num or enter q for quiting the game:"))
    if guess == q:
        print("program is over")
        break
    guess = int(guess)
    
    if guess < number:
        print("Too low, try again")
    elif guess > number:
        print("too much")
    else:
        print("You guessed")
        break