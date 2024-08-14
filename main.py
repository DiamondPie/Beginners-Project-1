# IMPORTANT
# If you're using MAC or LINUX Device, to make automatic screen clearing
# You need to change line 48 & 95 to the following line:
# os.system('clear')

import os, time
from get_random_word import getRandomWord
# There is an amount of ~275000 words
# from https://github.com/lorenbrichter/Words

HMpics = [ 
        "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========", 
        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========", 
        "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========",
        "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="
]

def setWordLength():
    # Initial set of word length
    print("Would you like to set the length of word?")
    print("If the input is invalid, we will use 4 as default")
    l = input("> ")
    if l.isdigit():
        l = int(l)
        print("OK word length set to", l)
    else:
        l = 4
        print("Using default value of 4")
    
    return l

def main():
    LENGTH = setWordLength()
    print('Getting random word... Hopefully this wouldn\'t take too long')
    WORD = getRandomWord(LENGTH)

    if WORD is None:
        print('CRITICAL Cannot find word that has length', LENGTH)
        os._exit(1)
        
    current = ["_"] * len(WORD)
    guessed = set()
    errors = set()

    os.system('cls')
    while True:
        print('-- Welcome to hangman --')
        # print("The answer is", WORD) # Debugger not cheating
        print()
        print(HMpics[len(errors)])
        print()
        print("The current word:")
        print(" ".join(current))
        print("Wrong letters:", " ".join(errors) if errors else "*Nothing*")
        print()

        # Check the game status (if it is win or lose)
        if len(errors) >= len(HMpics)-1:
            # With this you can add your life by increase the length of HMpics 
            print("He died rip :(")
            print(f"The word is *{WORD}*")
            break
        elif "_" not in current: # No more letters need to guess
            print("You won!")
            print("You guessed", len(guessed), "times")
            print("You made", len(errors), "mistakes", '... did you see the answer?' if len(errors) == 0 else '')
            break

        print("Guess a letter!")
        ipt = input("> ").lower()
        if not (ipt.isalpha() and len(ipt) == 1):
            # NEEDS to be a single letter
            print("Invalid input!")
        
        elif ipt in guessed:
            print("You already guessed that letter!")

        elif ipt in WORD:
            print("Correct! Well done!")
            # Need iterating to prevent repeat letters in the word, like hello
            current = [WORD[i] if WORD[i] == ipt else current[i] for i in range(len(WORD))]
            # for i in range(len(WORD)):
            #     if WORD[i] == ipt:
            #         current[i] = ipt

        else: # Guess is wrong
            print("Not quite right.. but nice try!")
            errors.add(ipt)
        
        guessed.add(ipt)
        time.sleep(1)
        os.system('cls')

if __name__ == "__main__":
    main()
