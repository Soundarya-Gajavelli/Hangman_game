# Hangman game

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    for i in secretWord:
        if i in lettersGuessed:
            pass
        else:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    guessd = ""
    for i in secretWord:
        if i in lettersGuessed:
            guessd = guessd + i
        else:
            guessd = guessd + "_ "
    return guessd

def getAvailableLetters(lettersGuessed):
    s = string.ascii_lowercase
    for i in lettersGuessed:
        s= s.replace(i, "")
    return s

def hangman(secretWord):
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", str(len(secretWord)), "letters long.")
    n= 8
    lettersGuessed = []
    while n > 0:
        print("_ "*11)
        print("You have", str(n), "guesses left.")
        print("Available letters: " + getAvailableLetters(lettersGuessed))
        guess = input("Please guess a letter:" )
        guess = guess.lower()
        if guess in secretWord:
            if guess not in lettersGuessed:
                lettersGuessed.append(guess)
                print("Good guess:"+ getGuessedWord(secretWord, lettersGuessed))
            else:
                print("Oops! You've already guessed that letter:"+ getGuessedWord(secretWord, lettersGuessed))

        else:
            lettersGuessed.append(guess)
            n =n-1
            print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
        if isWordGuessed(secretWord, lettersGuessed) == True:
            break

    if isWordGuessed(secretWord, lettersGuessed) == True:
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was", str(secretWord)+".")
            

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
