import random

def loadWords(filename="words.txt"):
    #Loads a list of words from a file.
    try:
        with open(filename, 'r') as f:
            return f.read().splitlines()
    except FileNotFoundError:
        print(f"Error: Could not find the words file '{filename}'.")
        return []  #Return an empty list if error

def chooseWord(wordList):
    #Randomly chooses a word from the list
    if wordList:
        return random.choice(wordList)
    else:
        print("Error: The word list is empty.")
        return None

def playTheGame():
    #Implements the game
    wordList = loadWords()
    secretWord = chooseWord(wordList)

    if not secretWord:
        return  #stops the game if there was an error loading words

    guessedLetters = set()
    guessesRemaining = 3
    turns = 0

    print("Welcome to the Word Guessing Game. Let's begin!")

    while guessesRemaining > 0 and secretWord:
        print(f"Word: {displayWord(secretWord, guessedLetters)}")
        guess = input("Guess a letter or the whole word: ").lower()

        if len(guess) == 1 and guess.isalpha():
            guessedLetters.add(guess)
            if guess in secretWord:
                print("Correct!")
            else:
                print("Incorrect.")
            turns += 1
        elif guess == secretWord:
            print("You win!")
            break
        else:
            guessesRemaining -= 1
            if guessesRemaining > 0:
                print("Wrong word! You have", guessesRemaining, "guesses left.")

    if secretWord:
        print("The word was:", secretWord)

def displayWord(word, guessedLetters):
    #displays the word with unguessed letters replaced by underscores/spaces
    return " ".join(char if char in guessedLetters else "_" for char in word)

if __name__ == "__main__":
    playTheGame()
