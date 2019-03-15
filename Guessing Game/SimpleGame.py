"""implement the logic of a simple guessing game"""
import random
#gen random number to guess

numberToGuess = random.randint(0, 10)

for guessCounter in range(3):


    #ask user

    userGuess = int(input('So, what do you think is the number?  '))

    #check user input5

    if numberToGuess < userGuess:
        print("too hight")
    elif numberToGuess > userGuess:
            print("too low")
    else:
         print("Congrats")
         break

else: print("GameOver,try again later...") 
print(f"The Correct Number was:...({numberToGuess})") #f before the string helps display a varible

