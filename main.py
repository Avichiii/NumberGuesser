import random

randomNum = random.randint(1,100)

userGuess = None
guesses = 0
while (userGuess != randomNum):

    userGuess = int(input("Enter user guess Number:"))

    if (userGuess == randomNum):
        print("You Guess That Right :)")
    else:
        if(userGuess<randomNum):
            print("Guess a little bit higher")
        else:
            print("Guess a little bit lower")

    guesses += 1

print(f"the total number of user guesses are {guesses}")


with open("highscore.txt", "w") as f:
    a = f.write(str(guesses))

with open("highscore.txt", "r") as f:
    highscore = int(f.read())

with open("highscore.txt", "w") as f:
    print("woo you got the highscore")
    if (highscore > guesses):
        c = f.write(str(guesses))
    else:
        c = f.write(str(highscore))
        
