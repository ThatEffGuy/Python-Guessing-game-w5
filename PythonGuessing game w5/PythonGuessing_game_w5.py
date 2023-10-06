import random # random module
number = random.randint(0,50) # chooses a number in range

numberofguesses = 0 # Number count of guesses

while numberofguesses <10:   #While guess are less than 10 allow user to guess
    print("guess a number between 0 and 50")
    guess = input()
    guess = int(guess)

    numberofguesses = numberofguesses+1  #If guess is higher or lower then give hint and add 1 to counter
    if guess < number:
        print("Your guess is too low")
    if guess > number:
        print("Your guess is too high")

    if guess == number:  #if guess = number exit loop
        break

if guess == number:  #If guess right print number of tries
    print("You guessed the number in ", numberofguesses, "tries!")
else:   #If guess counter = 10. print answer
    print("You did not guess the number. The number was ",number)
