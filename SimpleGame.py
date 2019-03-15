"""Implements the logic of a simple guessing game"""
import random

class GuessingGame:
	def __init__(self):
		#generate a random number for the user to guess
		self._numberToGuess = random.randint(0,10)
	
	def playGame(self):
	
		#let user try until the guess correctly
		userGuess = -1

		while self._numberToGuess != userGuess:

			#ask user to guess the number
			userGuess = int(input('What do you think is the number?'))

			#check if the user guessed correctly
			if userGuess > self._numberToGuess:
				print('Sorry, your guess is too high, please try again')
			elif userGuess < self._numberToGuess:
				print('Sorry your number is too low, please try again')
		else:
			print('Congratulations, You have guessed correctly, You should now go and play the lottery')
		