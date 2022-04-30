from random_word import RandomWords
from termcolor import colored
import os

def clear():
     os.system('cls' if os.name=='nt' else 'clear')
     return("   ")


r = RandomWords()
word = r.get_random_word(minLength=5, maxLength=5, hasDictionaryDef="true")
word = word.upper()

guesses = []

def wordCheck(theGuess):
    guess = theGuess.upper()
    
    correct = 0
    current = []
    for i in range(5):
        
        if guess[i] == word[i]:
            current.append(colored(guess[i], 'green'))
            correct += 1
        elif guess[i] in word:
            current.append(colored(guess[i], 'yellow'))
        else:
            current.append(colored(guess[i], 'white'))
    if correct == 5:
        print("Correct!!")
        quit()
    return current


print(clear())
for count in range(6):
    print("Please guess a five letter word...")
    guess = input()
    while len(guess) != len(word):
        print("""That is not a five letter word
        
        Please guess a five letter word...""")
        guess = input
    guesses += wordCheck(guess)
    print(clear())
    z = 0
    for x in guesses:
        if z == 5:
            print()
            z = 0
        print (x, end="")
        z += 1
    print()
print("""The correct answer is...

""" + word)