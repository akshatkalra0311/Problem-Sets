# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
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



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()
#Wowww, so we have declared the wordlist as a Global Variable, that's nice...

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for c in secret_word :
        if c in letters_guessed :
            pass
        else :
            return False
    return True




def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    if letters_guessed == [] :
        return len(secret_word)* '_'

    guessed_word = ''
    for c in secret_word :
        if c in letters_guessed :
            guessed_word += c
        else :
            guessed_word += '_ '
    return guessed_word



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    letters = ''
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    for c in alphabets :
        if c in letters_guessed :
            pass
        else :
            letters += c
    return letters
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    #secret_word = 'tact'
    print('Welcome to the game Hangman!')
    length = len(secret_word)
    print("I'm thinking of a word that is", length , "letters long.")
    num = 6
    guessed_word = ''
    letters_guessed = []
    guessed_word = get_guessed_word(secret_word, letters_guessed)
    warnings = 3
    vowels = 'aeiou'
    print('You have', warnings,'warnings left.')
    #guessed_word is not being updated over here in this loop.
    while num > 0 and secret_word != guessed_word :
        print('----------')
        print('You have', num, 'guesses left.')
        print("Available letters:", get_available_letters(letters_guessed))
        guess = input('Please guess a letter :')
        #If you push the foregoing statement above the while loop, you will not have to repeat it ever time the loop runs twice no.

        if not guess.isalpha() :

            if warnings <= 0 :
                print('You have exhausted all your warnings by entering invalid letters:', guessed_word)
                num -= 1
                continue
            warnings -= 1
            print('Oops! That is not a valid letter. You have', warnings, 'warnings left:', guessed_word)
            continue

        if guess in letters_guessed :

            if warnings <= 0 :
                num -= 1
                print("You've already guessed that letter and apparently you've also exhausted all your warnings so you loose out on another guess.")
                continue
            warnings -= 1
            print('Oops! You have already guessed that letter. You now have', warnings, 'warnings left.')
            continue


        guess = guess.lower()
        letters_guessed.append(guess)
        guessed_word = get_guessed_word(secret_word, letters_guessed)

        if guess in secret_word :
            print('Good guess:', guessed_word)
            continue
        else :
            print('Oops! That letter is not in my word:', guessed_word)
            if guess in vowels :
                print('Since you tried your luck with a vowel that\'s not in my word, you lose out on 2 guesses for this letter. Tread safely ahead...')
                num -= 1
        num -= 1



    unique = []
    for i in range(length) :
        if secret_word[i] in unique :
            pass
        else :
            unique.append(secret_word[i])

    uni = len(unique)

    print('----------')
    if secret_word == guessed_word :
        print('Congratulation, you won!')
        score = num * uni
        print('Your total score for the game is:', score)
    else :
        print("Ouch, you've run out of all the guesses.")
        print('The word you were trying to reach was ...\n', secret_word)




# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = my_word.replace(' ', '')
    if len(my_word) != len(other_word) :
        return False
    #print('Do I ?')
    for c in range(len(my_word)) :
        if my_word[c] != '_' :
            if my_word[c] != other_word[c] :
                return False
        else :
            #print('Did I')
            continue
    #print('Do I come out')
    return True



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    hold = False
    print('Possible word matches are:')
    for word in wordlist :
        match = match_with_gaps(my_word, word)
        if match :
            print(word, end = ' ')
            hold = True
    if hold == False :
        print('No matches found.')




def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    #secret_word = 'arils'
    print('Welcome to the game Hangman!')
    length = len(secret_word)
    print("I'm thinking of a word that is", length, "letters long.")
    num = 6
    guessed_word = ''
    letters_guessed = []
    guessed_word = get_guessed_word(secret_word, letters_guessed)
    warnings = 3
    vowels = 'aeiou'
    print('You have', warnings, 'warnings left.')
    # guessed_word is not being updated over here in this loop.
    while num > 0 and secret_word != guessed_word:
        print('\n----------')
        print('You have', num, 'guesses left.')
        print("Available letters:", get_available_letters(letters_guessed))
        guess = input('Please guess a letter :')
        # If you push the foregoing statement above the while loop, you will not have to repeat it every time the loop runs twice no.

        if guess == '*':
            show_possible_matches(guessed_word)
            continue

        if not guess.isalpha():

            if warnings <= 0:
                print('You have exhausted all your warnings by entering invalid letters:', guessed_word)
                num -= 1
                continue
            warnings -= 1
            print('Oops! That is not a valid letter. You have', warnings, 'warnings left:', guessed_word)
            continue

        if guess in letters_guessed:

            if warnings <= 0:
                num -= 1
                print(
                    "You've already guessed that letter and apparently you've also exhausted all your warnings so you loose out on another guess.")
                continue
            warnings -= 1
            print('Oops! You have already guessed that letter. You now have', warnings, 'warnings left.')
            continue

        guess = guess.lower()
        letters_guessed.append(guess)
        guessed_word = get_guessed_word(secret_word, letters_guessed)
        
        
        if guess in secret_word:
            print('Good guess:', guessed_word)
            continue
        else:
            print('Oops! That letter is not in my word:', guessed_word)
            if guess in vowels:
                print(
                    'Since you tried your luck with a vowel that\'s not in my word, you lose out on 2 guesses for this letter. Tread safely ahead...')
                num -= 1
        num -= 1

    unique = []
    for i in range(length):
        if secret_word[i] in unique:
            pass
        else:
            unique.append(secret_word[i])

    uni = len(unique)

    print('----------')
    if secret_word == guessed_word:
        print('Congratulations, you won !!')
        score = num * uni
        print('Your total score for the game is:', score)
    else:
        print("Ouch, you've run out of all the guesses.")
        print('The word you were trying to reach is ...\n', secret_word)

# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

    #hangman('tact')
###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    #hangman_with_hints('arils')

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
