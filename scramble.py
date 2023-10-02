import time
import sys
import random
from string import punctuation

try:
    from nltk.corpus import cmudict    
except ImportError:
    print("""You need the the above cmudict to run this program.
          Use the following instructions to download it:
            1- Open your Command Window or Terminal
            2- Enter: python -m pip install nltk
            3- Once downloaded start pyhton in your terminal with: 
                python or python3 depending on your used version
            4- Enter: import nltk
            5- If step 4 draws no error enter: nltk.download()
            6- Select the Corpora tab
            7- Select cmudict & click Download
            8- Once download is finished, close the window and terminal and retry this Program""")

cmudict = cmudict.dict()
words = []
guesses = 0
maxGuesses = 4 # Starts at 0, so 0-4 is 5 guesses
score = 0

def shuffle_word(word):
    lst = [*word]
    random.shuffle(lst)
    return ''.join(lst)

for word in cmudict:
    word = word.lower().strip(punctuation)
    words.append(word)

while True:
    keyWord = random.choice(words)
    scrambledWord = shuffle_word(keyWord)

    while True:
        guess = input(f"\nPlease try to unscramble this word: {scrambledWord}\n\t> ")
        if guess == scrambledWord:
            print(f"You're right, {guess} was the answer!")
            score += 1
        elif guess != scrambledWord:
            if guesses < maxGuesses:
                print(f"{guess} is incorrect, try again!\n\n")
                guesses += 1
            elif guesses == maxGuesses:
                print(f"{guess} is incorrect\nThe correct word was {keyWord}")
                time.sleep(2.5)
                print(f"You got {score} words right")
                time.sleep(2.5)
                guesses = guesses - 4
                break

    end = input("\nDo you wish to play again: y/n\n\t> ")
    if end == 'y':
        continue
    elif end == 'n':
        print("Thanks for playing!")
        time.sleep(2)
        sys.exit()