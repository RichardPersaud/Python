#imports random
import random

#creates a random interger from 0 to 10
randNum = random.randint(0, 10)

#creates a random real number
realRand = random.random()

#creates a random range
funkyRand = random.randrange(0, 100, 7)

# prints the random number
print(f"A random number between 0 and 10 is {randNum}")
print(f"A random real is {realRand}")
print(f"A random range {funkyRand}")