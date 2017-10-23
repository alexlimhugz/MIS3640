# Hangman game
#


import random

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
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
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
      if letter in lettersGuessed:
        return True
      else:
        return False

# When you've completed your function isWordGuessed, uncomment these three lines
# and run this file to test!

# secretWord = 'apple'
# lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(isWordGuessed(secretWord, lettersGuessed))

# Expected output:
# False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    result = ''
    guessedClue = ''
    for letter in secretWord:
      if letter letterGuessed:
        result = letter + ' '
      else:
        result = "_ "
      guessedClue - guessClue + result
    return 'Letters You\'ve Guessed: ' + guessedClue



# When you've completed your function getGuessedWord, uncomment these three lines
# and run this file to test!

# secretWord = 'apple'
# lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(getGuessedWord(secretWord, lettersGuessed))

# Expected output:
# '_ pp_ e'


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # Hint: You might consider using string.ascii_lowercase, which
    # is a string comprised of all lowercase letters.
    import string
    alphabet = string.ascii_lowercase

    result = ''
    lettersRemain = ''

    for letter in alphabet:
      if letter in lettersGuessed:
        lettersRemain = ''
      else:
        result = letter
      lettersRemain = lettersRemain + result

    return lettersRemain


# When you've completed your function getAvailableLetters, uncomment these two lines
# and run this file to test!

# lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(getAvailableLetters(lettersGuessed))

# Expected output:
# abcdfghjlmnoqtuvwxyz


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print 'Welcome to Hangman!'
    print 'Your secret word is ' + str(len(secretWord)) + ' letters long.'
    guessLeft = 8
    lettersGuessed = []
    while guessLeft>0 and not isWordGuessed(secretWord, lettersGuessed):
      print 'You have ' + str(guessLeft) + ' guessed left.'
      print 'Available letters:' + getAvailableLetters(lettersGuessed)
      guess = str(raw_input('Please guess a letter: '))
      guess - guess.lower()
      while len(guess) !=1 and guess not in string.ascii_lowercase:
        guess = str(raw_input('Please guess a letter: '))
      if guess not in lettersGuessed:
        lettersGuessed.append(guess)
        if guess in secretWord:
          print 'Great guess!'
        else:
          guessLeft-=1
          print 'Sorry! That letter is not in the Secret Word.'
      else:
        print 'You already guessed that letter.'
      print getGuessedWord(secretWord, lettersGuessed)
    if isWordGuessed(secretWord, lettersGuessed):
      print 'Look at you! You guessed the Secret Word!'
    else:
      print 'Sorry. Out of guessed. The word was', + str(secretWord) + ' .'
      




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
