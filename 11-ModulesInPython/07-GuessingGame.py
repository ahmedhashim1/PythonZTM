from random import randint
import sys

# generate a number between 1 to 10
# answer = randint(1, 10)) # using randomint to provide range of target guess
answer = randint(int(sys.argv[1]), int(sys.argv[2]))  # we are now passing random range via file argument
# input from user

# check the input is a number 1~10
while True:
    try:
        guess = int(input("Guess a number between 1 and 10: "))
        # print(answer)
        if 0 < guess < 11:
            if guess == answer:
                print("You guessed right!")
                break
        else:
            print("Number not in range.")
    except ValueError:
        print("Please enter a number.")
        continue
# check if the guess is right, otherwise ask again
