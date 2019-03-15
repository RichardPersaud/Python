"""implement the logic of a simple guessing game"""
import random

class GuessingGame:
    def __init__(self):
        #gen random number to guess
        self._numberToGuess = random.randint(0,10)


    def playGame(self):

        userGuess = -1
        while self._numberToGuess != userGuess:
            #ask user
            userGuess = int(input('So, what do you think is the number?  '))

            #check user input

            if self._numberToGuess < userGuess:
                print("too hight")
            elif self._numberToGuess > userGuess:
                    print("too low")

        else: print("Congrats..")
    