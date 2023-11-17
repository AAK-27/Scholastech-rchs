from random import randint

options = ("rock", "paper", "scissors")

while True:
    guess = ""
    while not (guess in options):
        guess = input("Enter rock, paper, or scissors: ").strip().lower()
        if guess == "end":
            exit()
    print("You guessed " + guess + "!")
    computer = randint(0,2)
    print("Computer guessed " + options[computer] + "!")
    guess = options.index(guess)
    if guess == computer:
        print("-You Tied-")
    elif (computer-guess == 1) or (guess-computer == 2):
        print("~You Lost~")
    else:
        print("!You Won!")